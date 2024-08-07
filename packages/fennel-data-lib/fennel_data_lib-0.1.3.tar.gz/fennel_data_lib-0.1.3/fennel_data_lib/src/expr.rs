use crate::rowcol::Col;
use serde::Serialize;
use crate::arrow_lib::{to_arrow_field, to_arrow_dtype};
use crate::{types::Type, value::Value};
use anyhow::{anyhow, bail, Result};
use builders::{lit, when};
use datafusion_common::scalar::ScalarValue;
use datafusion_expr::{self as lexpr, Expr as ArrowLogicalExpr};
use datafusion_functions::expr_fn;
use datafusion_functions_array::expr_fn as array_fn;
use itertools::Itertools;
use std::fmt;
use std::sync::Arc;
use uuid::Uuid;
use crate::types::StructType;
use crate::schema::Schema;
use crate::schema::Field;
use crate::types::DecimalType;

use crate::schema_proto::expr::Expr as ProtoExpr;
use crate::schema_proto::expr as eproto;

#[derive(Clone, PartialEq, Serialize)]
pub enum Expr {
    Ref {
        name: String,
    },
    Lit {
        value: Value,
    },
    // NOTE: Cast should not be exposed to the user, it is only used internally
    // to safely cast types.
    Cast {
        expr: Box<Expr>,
        dtype: Type,
    },
    Unary {
        op: UnOp,
        expr: Box<Expr>,
    },
    Binary {
        op: BinOp,
        left: Box<Expr>,
        right: Box<Expr>,
    },
    Case {
        when_thens: Vec<(Expr, Expr)>,
        otherwise: Option<Box<Expr>>, // if none, treated as None literal
    },
    // Given expression, checks if it is null. Expr can be of any type
    // always returns a boolean (not optional)
    IsNull {
        expr: Box<Expr>,
    },
    // Given expression, returns the default if it is null, otherwise the
    // expression itself. Expr can be of any type. Expr & default should be
    // promotable to the same type
    FillNull {
        expr: Box<Expr>,
        default: Box<Expr>,
    },
    ListFn {
        list: Box<Expr>,
        func: Box<ListFn>,
    },
    MathFn {
        func: MathFn,
        expr: Box<Expr>,
    },
    StructFn {
        struct_: Box<Expr>,
        func: Box<StructFn>,
    },
    DictFn {
        dict: Box<Expr>,
        func: Box<DictFn>,
    },
    StringFn {
        func: Box<StringFn>,
        expr: Box<Expr>,
    },
}


#[derive(Clone, Debug, PartialEq, Serialize)]
pub enum StringFn {
    Len,
    ToLower,
    ToUpper,
    Contains { key: Expr },
    StartsWith { key: Expr },
    EndsWith { key: Expr },
    Concat { other: Expr },
}

#[derive(Clone, Debug, PartialEq, Serialize)]
pub enum DictFn {
    Len,
    Get { key: Expr, default: Option<Expr> },
    Contains { key: Expr },
}

#[derive(Clone, Debug, PartialEq, Serialize)]
pub enum ListFn {
    Len,
    HasNull,
    Get { index: Expr },
    Contains { item: Expr },
}

#[derive(Clone, Debug, PartialEq, Serialize)]
pub enum StructFn {
    Get { field: String },
}

/// A compiled expression is an expression that has been validated
/// and type-checked against a schema and has a known output type.
#[derive(Clone, Debug, PartialEq, Serialize)]
pub struct CompiledExpr {
    rewritten: Expr,
    original: Expr,
    schema: Arc<Schema>,
    dtype: Type,
}

impl CompiledExpr {
    pub fn expand(&self, len: usize, cols: &mut Vec<Col>) -> Self {
        let rewritten = self.rewritten.expand(len, cols);
        Self {
            rewritten,
            original: self.original.clone(),
            schema: self.schema.clone(),
            dtype: self.dtype.clone(),
        }
    }

    pub fn org_expr(&self) -> &Expr {
        &self.original
    }
    /// Checks if the given type CAN be made to match the expression.
    ///
    /// For instance, if the expression naturally evaluates to an int, it will
    /// match int, float, optional[int], or optional[float] but won't match
    /// string, list[int], or optional[string] etc.
    ///
    /// The only exception is synthetic types like between, oneof, regex etc.
    pub fn matches(&self, dtype: &Type) -> bool {
        match (&self.dtype, dtype) {
            (t1, t2) if promotable(t1, t2) => true,
            (t, Type::Between(b)) => t == b.dtype(),
            (t, Type::OneOf(o)) => t == o.dtype(),
            (Type::String, Type::Regex(_)) => true,
            _ => false,
        }
    }

    /// Returns the output type of the expression
    pub fn dtype(&self) -> &Type {
        &self.dtype
    }

    /// Given a type, add casts, if necessary, to the expression
    /// to safely cast it to the given type
    fn safecast(&self, dtype: &Type) -> Result<Expr> {
        if self.dtype == *dtype {
            return Ok(self.rewritten.clone());
        }
        // there are only 2 valid cases of casting:
        // 1. going from t -> senior(t)
        // 2. going from optional[t] -> senior(t) -- we accept this to be a safe
        // promotion since arrow doesn't distinguish between null and non-null
        // we can combine these two cases by checking senior of inner type
        let inner = self.dtype.inner();
        if promotable(inner, dtype) {
            return Ok(Expr::Cast {
                expr: Box::new(self.rewritten.clone()),
                dtype: dtype.clone(),
            });
        }
        bail!(
            "can not safely cast expression {:?} of type {:?} to {:?}",
            self.rewritten,
            self.dtype,
            dtype,
        );
    }
}

/// Returns true if the given type can be promoted to the target type
fn promotable(from: &Type, to: &Type) -> bool {
    use Type::*;
    match (from, to) {
        (t1, t2) if t1 == t2 => true,
        (Null, Optional(_)) => true,
        (Optional(t1), Optional(t2)) => promotable(t1, t2),
        (t1, Optional(t2)) => promotable(t1, t2),
        (Int, Float) => true,
        _ => false,
    }
}

/// Given a type, returns the list of senior types that it can be promoted to
/// The senior are given in the order of seniority, from most junior to most senior
fn seniors(of: &Type) -> Option<Vec<Type>> {
    use Type::*;
    match of {
        Null => None,
        Int => Some(vec![Int, Type::optional(Int), Float, Type::optional(Float)]),
        Optional(t) => match t.as_ref() {
            Null => None,
            Int => Some(vec![Type::optional(Int), Type::optional(Float)]),
            _ => Some(vec![of.clone()]),
        },
        Between(b) => seniors(b.dtype()),
        OneOf(o) => seniors(o.dtype()),
        Regex(_) => seniors(&Type::String),
        non_optional => Some(vec![
            non_optional.clone(),
            Type::optional(non_optional.clone()),
        ]),
    }
}

/// Given two types, return the least common ancestor if one exists
fn lca(t1: &Type, t2: &Type) -> Option<Type> {
    use Type::*;
    match (t1, t2) {
        (Null, Null) => Some(Null),
        (Null, t) | (t, Null) => Some(Type::optional(t.clone())),
        (t1, t2) => {
            let seniors1 = seniors(t1)?;
            let seniors2 = seniors(t2)?;
            let mut common = seniors1
                .iter()
                .filter(|t1| seniors2.iter().any(|t2| t1 == &t2))
                .collect_vec();
            common.sort_by(|t1, t2| {
                let i1 = seniors1.iter().position(|t| &t == t1).unwrap();
                let i2 = seniors1.iter().position(|t| &t == t2).unwrap();
                i1.cmp(&i2)
            });
            match common.first() {
                Some(t) => Some((*t).clone()),
                None => None,
            }
        }
    }
}

impl Expr {
    /// Replaces each literal in the expression with a reference to a column of
    /// the same literal repeated `len` times. Also returns a vector of the
    /// columns
    fn expand(&self, len: usize, cols: &mut Vec<Col>) -> Self {
        match self {
            Self::Lit { value } => {
                for col in cols.iter() {
                    if col.values()[0] == *value {
                        return Self::Ref {
                            name: col.name().to_string(),
                        };
                    }
                }
                // generate a random name
                let name = Uuid::new_v4().to_string();
                let field = Arc::new(Field::new(name.clone(), natural_type(value)));
                let col = Col::new(field, Arc::new(vec![value.clone(); len])).unwrap();
                cols.push(col);
                Self::Ref { name }
            }
            Self::ListFn { list, func } => {
                let list = Box::new(list.expand(len, cols));
                let func = match func.as_ref() {
                    ListFn::Len => ListFn::Len,
                    ListFn::Get { index } => ListFn::Get {
                        index: index.expand(len, cols),
                    },
                    ListFn::HasNull => ListFn::HasNull,
                    ListFn::Contains { item } => {
                        let item = item.expand(len, cols);
                        ListFn::Contains { item }
                    }
                };
                Self::ListFn {
                    list,
                    func: Box::new(func),
                }
            }
            Self::DictFn { dict, func } => {
                let dict = Box::new(dict.expand(len, cols));
                let func = match func.as_ref() {
                    DictFn::Len => DictFn::Len,
                    DictFn::Get { key, default } => DictFn::Get {
                        key: key.expand(len, cols),
                        default: default.as_ref().map(|d| d.expand(len, cols)),
                    },
                    DictFn::Contains { .. } => todo!(),
                };
                Self::DictFn {
                    dict,
                    func: Box::new(func),
                }
            }
            Self::StringFn { func, expr } => {
                let expr = Box::new(expr.expand(len, cols));
                let func = match func.as_ref() {
                    StringFn::Len => StringFn::Len,
                    StringFn::ToLower => StringFn::ToLower,
                    StringFn::ToUpper => StringFn::ToUpper,
                    StringFn::Contains { key } => StringFn::Contains {
                        key: key.expand(len, cols),
                    },
                    StringFn::StartsWith { key } => StringFn::StartsWith {
                        key: key.expand(len, cols),
                    },
                    StringFn::EndsWith { key } => StringFn::EndsWith {
                        key: key.expand(len, cols),
                    },
                    StringFn::Concat { other } => StringFn::Concat {
                        other: other.expand(len, cols),
                    }
                };
                Self::StringFn {
                    func: Box::new(func),
                    expr,
                }
            }
            Self::StructFn { struct_, func } => {
                let struct_ = Box::new(struct_.expand(len, cols));
                let func = match func.as_ref() {
                    StructFn::Get { field } => StructFn::Get {
                        field: field.clone(),
                    },
                };
                Self::StructFn {
                    struct_,
                    func: Box::new(func),
                }
            }
            Self::Ref { .. } => self.clone(),
            Self::Unary { op, expr } => Self::Unary {
                op: *op,
                expr: Box::new(expr.expand(len, cols)),
            },
            Self::Binary { op, left, right } => Self::Binary {
                op: *op,
                left: Box::new(left.expand(len, cols)),
                right: Box::new(right.expand(len, cols)),
            },
            Self::Case {
                when_thens,
                otherwise,
            } => Self::Case {
                when_thens: when_thens
                    .iter()
                    .map(|(w, t)| (w.expand(len, cols), t.expand(len, cols)))
                    .collect(),
                otherwise: otherwise.as_ref().map(|o| Box::new(o.expand(len, cols))),
            },
            Self::Cast { expr, dtype } => Self::Cast {
                expr: Box::new(expr.expand(len, cols)),
                dtype: dtype.clone(),
            },
            Self::FillNull { expr, default } => Self::FillNull {
                expr: Box::new(expr.expand(len, cols)),
                default: Box::new(default.expand(len, cols)),
            },
            Self::IsNull { expr } => Self::IsNull {
                expr: Box::new(expr.expand(len, cols)),
            },
            Self::MathFn { func, expr } => Self::MathFn {
                func: *func,
                expr: Box::new(expr.expand(len, cols)),
            },
        }
    }

    pub fn compile(&self, schema: Arc<Schema>) -> Result<CompiledExpr> {
        use Type::*;
        match self {
            Expr::Lit { value } => Ok(CompiledExpr {
                rewritten: self.clone(),
                original: self.clone(),
                schema,
                dtype: natural_type(value),
            }),
            Expr::Ref { name } => match schema.find(name) {
                None => bail!("field '{}' not found in the schema", name),
                Some(field) => Ok(CompiledExpr {
                    rewritten: self.clone(),
                    original: self.clone(),
                    schema: schema.clone(),
                    dtype: field.dtype().clone(),
                }),
            },
            Expr::ListFn { list, func } => {
                let list = list.compile(schema.clone())?;
                let dtype = list.dtype();
                let eltype = match dtype.inner() {
                    List(l) => l.as_ref().clone(),
                    Embedding(_) => Float,
                    _ => bail!("invalid expression: expected list but found {:?}", dtype),
                };
                // compute the output type assuming the list is not optional
                match func.as_ref() {
                    ListFn::Contains { item } => {
                        let item = item.compile(schema.clone())?;
                        match item.dtype() {
                            t if promotable(t, &eltype) => {
                                let item = item.safecast(&eltype)?;
                                let mut when_thens = vec![];
                                // if item is nullable, we need to check for null
                                if matches!(t, Null | Optional(_)) {
                                    when_thens.push((
                                        Expr::IsNull { expr: Box::new(item.clone()) },
                                        none_as(&Type::optional(Bool)),
                                    ));
                                }
                                let rewritten = Expr::Case {
                                    // if expr is null, output is null
                                    // otherwise, output is list.contains(item)
                                    when_thens: vec![(
                                            Expr::IsNull { expr: Box::new(item.clone()) },
                                            none_as(&Type::optional(Bool)),
                                    ),
                                    (
                                        Expr::ListFn {
                                            list: Box::new(list.rewritten.clone()),
                                            func: Box::new(ListFn::Contains { item: item.clone() }),
                                        },
                                        Expr::ListFn {
                                            list: Box::new(list.rewritten.clone()),
                                            func: Box::new(ListFn::Contains { item: item.clone() }),
                                        },
                                    ),
                                    (
                                        Expr::ListFn { 
                                            list: Box::new(list.rewritten.clone()),
                                            func: Box::new(ListFn::HasNull),
                                        },
                                        none_as(&Type::optional(Bool)),
                                    )],
                                    otherwise: Some(Box::new(Expr::Lit{ value: Value::Bool(false)})),
                                };
                                // if element can be null, we need to output optional bool
                                let outtype = match &eltype {
                                    Optional(_) => Type::optional(Bool),
                                    _ => Bool,
                                };
                                // if list is optional, output is optional bool else bool
                                // if list is None, output is None
                                let (outtype, rewritten) = match &dtype {
                                    Optional(_) => (Type::optional(outtype), Expr::Case { 
                                        when_thens: vec![(
                                            Expr::IsNull { expr: Box::new(list.rewritten.clone()) },
                                            none_as(&Type::optional(Bool)),
                                        )],
                                        otherwise: Some(Box::new(rewritten.clone())),
                                    }),
                                    _ => (outtype, rewritten),
                                };
                                Ok(CompiledExpr {
                                    rewritten,
                                    original: self.clone(),
                                    schema,
                                    dtype: outtype
                                })
                            },
                            _ => bail!(
                                "invalid expression: expected item to be of type {:?} but found {:?}",
                                eltype,
                                item.dtype()
                            ),
                        }
                    }
                    ListFn::HasNull => {
                        // if element type is not null or optional, output is false
                        let rewritten = match &eltype {
                            Null | Optional(_) => {
                                Expr::ListFn {
                                    list: Box::new(list.rewritten.clone()),
                                    func: Box::new(ListFn::HasNull),
                                }
                            }
                            _ => Expr::Lit { value: Value::Bool(false) },
                        };
                        // if list is optional, output is optional bool else bool
                        // if list is None, output is None
                        let (outtype, rewritten) = match &dtype {
                            Optional(_) => (Type::optional(Bool), Expr::Case {
                                when_thens: vec![(
                                    Expr::IsNull { expr: Box::new(list.rewritten.clone()) },
                                    none_as(&Type::optional(Bool)),
                                )],
                                otherwise: Some(Box::new(rewritten.clone())),
                            }),
                            _ => (Bool, rewritten),
                        };
                        Ok(CompiledExpr {
                            rewritten,
                            original: self.clone(),
                            schema,
                            dtype: outtype,
                        })
                    }
                    _ => {
                        // compute the output type assuming the list is not optional
                        let (outtype, func) = match func.as_ref() {
                            ListFn::Len => (Int, ListFn::Len),
                            ListFn::Get { index } => {
                                let index = index.compile(schema.clone())?;
                                match index.dtype() {
                                    // accessing out of bounds index returns None
                                    // so output type is optional[eltype]
                                    Int => (Type::optional(eltype.clone()), ListFn::Get { index: index.rewritten }),
                                    _ => bail!(
                                        "invalid expression: expected index to be of int type but found {:?}",
                                        index.dtype()
                                    ),
                                }
                            }
                            ListFn::HasNull => unreachable!("handled separately"),
                            ListFn::Contains { .. } => unreachable!("handled separately"),
                        };
                        // adjust the output type if the list is optional
                        let outtype = match &dtype {
                            Optional(_) => Type::optional(outtype),
                            _ => outtype,
                        };
                        Ok(CompiledExpr {
                            rewritten: Expr::ListFn {
                                list: Box::new(list.rewritten),
                                func: Box::new(func),
                            },
                            original: self.clone(),
                            schema,
                            dtype: outtype,
                        })
                    }
                }
            }
            Expr::StructFn { struct_, func } => {
                let struct_ = struct_.compile(schema.clone())?;
                let dtype = struct_.dtype();
                let stype = match dtype.inner() {
                    Struct(s) => s.as_ref(),
                    _ => bail!("invalid expression: expected struct but found {:?}", dtype),
                };
                // compute the output type assuming the struct is not optional
                let (outtype, func) =
                    match func.as_ref() {
                        StructFn::Get { field } => {
                            let field = stype.fields().iter().find(|f| f.name() == field).ok_or(
                                anyhow!(
                                    "invalid expression: field '{}' not found in struct {:?}",
                                    field,
                                    stype
                                ),
                            )?;
                            (field.dtype().clone(), func.as_ref().clone())
                        }
                    };
                // adjust the output type if the struct is optional
                let outtype = match &dtype {
                    Optional(_) => Type::optional(outtype),
                    _ => outtype,
                };
                Ok(CompiledExpr {
                    rewritten: Expr::StructFn {
                        struct_: Box::new(struct_.rewritten),
                        func: Box::new(func),
                    },
                    original: self.clone(),
                    schema,
                    dtype: outtype,
                })
            }
            Expr::DictFn { dict, func } => {
                let dict = dict.compile(schema.clone())?;
                let dtype = dict.dtype();
                let eltype = match dtype.inner() {
                    Map(m) => m.as_ref().clone(),
                    _ => bail!("invalid expression: expected dict but found {:?}", dtype),
                };
                // compute the output type assuming the dict is not optional
                let (outtype, func) = match func.as_ref() {
                    DictFn::Len => (Int, DictFn::Len),
                    DictFn::Get { key, default } => {
                        let key = key.compile(schema.clone())?;
                        let default = default
                            .as_ref()
                            .map(|d| d.compile(schema.clone()))
                            .transpose()?;
                        match key.dtype() {
                            String => (eltype.clone(), DictFn::Get {
                                key: key.rewritten,
                                default: default.map(|d| d.rewritten),
                            }),
                            _ => bail!(
                                "invalid expression: expected key to be of string type but found {:?}",
                                key.dtype()
                            ),
                        }
                    }
                    DictFn::Contains { .. } => todo!(),
                };
                // adjust the output type if the dict is optional
                let outtype = match &dtype {
                    Optional(_) => Type::optional(outtype.clone()),
                    _ => outtype.clone(),
                };
                Ok(CompiledExpr {
                    rewritten: Expr::DictFn {
                        dict: Box::new(dict.rewritten),
                        func: Box::new(func),
                    },
                    original: self.clone(),
                    schema,
                    dtype: outtype,
                })
            }
            Expr::StringFn { func, expr } => {
                let expr = expr.compile(schema.clone())?;
                match expr.dtype().inner() {
                    Null | String => {}
                    _ => bail!(
                        "invalid expression: expected string type for function '{:?}' but found {:?}",
                        func,
                        expr.dtype(),
                    ),
                }

                fn compile_sub_expr(sub_expr: &Expr, schema: Arc<Schema>, func: &Box<StringFn>) -> Result<CompiledExpr> {
                    let sub_expr = sub_expr.compile(schema)?;
                    match sub_expr.dtype() {
                        String => Ok(sub_expr),
                        _ => bail!(
                            "invalid sub_expr: expected string type for function '{:?}' but found {:?}",
                            func,
                            sub_expr.dtype()
                        )
                    }
                }
                let func = match func.as_ref() {
                    StringFn::Len => StringFn::Len,
                    StringFn::ToLower => StringFn::ToLower,
                    StringFn::ToUpper => StringFn::ToUpper,
                    StringFn::Contains { key } => {
                        let key = compile_sub_expr(key, schema.clone(), func)?;
                        let key = key.rewritten;
                        StringFn::Contains { key }
                    },
                    StringFn::StartsWith { key } => {
                        let key = compile_sub_expr(key, schema.clone(), func)?;
                        let key = key.rewritten;
                        StringFn::StartsWith { key }
                    },
                    StringFn::EndsWith { key } => {
                        let key = compile_sub_expr(key, schema.clone(), func)?;
                        let key = key.rewritten;
                        StringFn::EndsWith { key }
                    },
                    StringFn::Concat { other } => {
                        let other = compile_sub_expr(other, schema.clone(), func)?;
                        let other = other.rewritten;
                        StringFn::Concat { other }
                    },
                };

                // compute the output type assuming the string is not optional
                let (outtype, func) = match func {
                    StringFn::Len => (Int, StringFn::Len),
                    StringFn::ToLower | StringFn::ToUpper | StringFn::Concat { .. } => (String, func),
                    StringFn::Contains { .. } | StringFn::StartsWith { .. } | StringFn::EndsWith { .. } => (Bool, func),
                };
                let rewritten = Expr::StringFn {
                    func: Box::new(func),
                    expr: Box::new(expr.rewritten.clone()),
                };
                // adjust the output type if the string is optional
                let (outtype, rewritten) = match expr.dtype() {
                    Null => (Type::optional(outtype.clone()), Expr::Cast { expr: Box::new(lit(Value::None)), dtype: Type::optional(outtype.clone()) }),
                    Optional(_) => (Type::optional(outtype.clone()), rewritten),
                    String => (outtype.clone(), rewritten),
                    _ => unreachable!(),
                };
                Ok(CompiledExpr {
                    rewritten,
                    original: self.clone(),
                    schema,
                    dtype: outtype,
                })
            }
            Expr::MathFn { func, expr } => {
                // Validate: expr can be promoted to a numeric type
                let expr = expr.compile(schema.clone())?;
                if !promotable(expr.dtype(), &Type::optional(Float)) {
                    bail!(
                        "invalid expression: math function {} expected argument to be of numeric type but found {:?}",
                        func,
                        expr.dtype()
                    );
                }

                match func {
                    MathFn::Ceil | MathFn::Floor => {
                        // ceil/floor always returns an integer, maybe optional
                        let outtype = match &expr.dtype {
                            Null | Optional(_) => Type::optional(Int),
                            _ => Int,
                        };
                        let rewritten = Expr::Cast {
                            expr: Box::new(Expr::MathFn {
                                func: *func,
                                expr: Box::new(expr.safecast(&Type::optional(Float))?),
                            }),
                            dtype: outtype.clone(),
                        };
                        Ok(CompiledExpr {
                            rewritten,
                            original: self.clone(),
                            schema,
                            dtype: outtype,
                        })
                    },
                    MathFn::Round { precision } => {
                        // round returns an int when precision is 0 and float otherwise, maybe optional
                        let outtype = match (&expr.dtype, precision) {
                            (Null | Optional(_), None | Some(0)) => Type::optional(Int),
                            (Null | Optional(_), _) => Type::optional(Float),
                            (_, None | Some(0)) => Int,
                            (_, _) => Float,
                        };
                        let rewritten = Expr::Cast {
                            expr: Box::new(Expr::MathFn {
                                func: *func,
                                expr: Box::new(expr.safecast(&Type::optional(Float))?),
                            }),
                            dtype: outtype.clone(),
                        };
                        Ok(CompiledExpr {
                            rewritten,
                            original: self.clone(),
                            schema,
                            dtype: outtype
                        })
                    },
                    MathFn::Abs => {
                        let outtype = match &expr.dtype {
                            Null => Type::optional(Int),
                            Optional(t) if t.as_ref().eq(&Int) => Type::optional(Int),
                            Optional(_) => Type::optional(Float),
                            Int => Int,
                            _ => Float,
                        };
                        let rewritten = Expr::Cast {
                            expr: Box::new(Expr::MathFn {
                                func: *func,
                                expr: Box::new(expr.safecast(&Type::optional(Float))?),
                            }),
                            dtype: outtype.clone(),
                        };
                        Ok(CompiledExpr {
                            rewritten,
                            original: self.clone(),
                            schema,
                            dtype: outtype,
                        })
                    }
                }
            },
            Expr::Unary { op, expr } => match op {
                UnOp::Not => {
                    let predicate = expr.compile(schema.clone())?;
                    // 1. Validate: predicate can be promoted to a boolean
                    if !promotable(predicate.dtype(), &Type::optional(Bool)) {
                        bail!("invalid expression: expected boolean expression");
                    }
                    // 2. Find output type: either a boolean or optional boolean
                    let outtype = match &predicate.dtype {
                        Bool => Bool,
                        Null => Type::optional(Bool),
                        Optional(t) if t.as_ref().eq(&Bool) => Type::optional(Bool),
                        _ => unreachable!(),
                    };

                    // 3. Rewrite: use null if predicate is null
                    let rewritten = match &predicate.dtype {
                        Null => Expr::Lit { value: Value::None },
                        _ => self.clone(),
                    };

                    Ok(CompiledExpr {
                        rewritten,
                        original: self.clone(),
                        schema,
                        dtype: outtype,
                    })
                }
                UnOp::Neg => {
                    let expr = expr.compile(schema.clone())?;
                    // 1. Validate: expr can be promoted to a numeric type
                    if !promotable(expr.dtype(), &Type::optional(Float)) {
                        bail!(
                            "invalid expression: expected numeric type but found {:?}",
                            expr.dtype()
                        );
                    }
                    // 2. Find output type: either a float or optional float
                    let outtype = match &expr.dtype {
                        Int => Int,
                        Float => Float,
                        Null => Type::optional(Float),
                        Optional(t) if t.as_ref().eq(&Int) => Type::optional(Int),
                        Optional(t) if t.as_ref().eq(&Float) => Type::optional(Float),
                        _ => unreachable!(),
                    };
                    // 3. Rewrite: use null if expr is null
                    let rewritten = match &expr.dtype {
                        Null => Expr::Lit { value: Value::None },
                        _ => self.clone(),
                    };
                    Ok(CompiledExpr {
                        rewritten,
                        original: self.clone(),
                        schema,
                        dtype: outtype,
                    })
                }
                UnOp::Len => {
                    todo!()
                }
            },
            Expr::Binary { op, left, right } if matches!(op, BinOp::FloorDiv) => {
                let left = left.compile(schema.clone())?;
                let right = right.compile(schema.clone())?;
                let ltype = left.dtype();
                let rtype = right.dtype();
                // 1. Validate: both sides can be promoted to a numeric type
                let max = Type::optional(Float);
                if !promotable(ltype, &max) || !promotable(rtype, &max) {
                    bail!(
                        "invalid expression: both sides of '{}' must be numeric types but found {} & {}",
                        op,
                        ltype,
                        rtype
                    );
                }
                // can unwrap because we know both are numerics, so lca exists
                let common = lca(ltype, rtype).unwrap();
                // 2. Find output type: either int, or float, or options
                let outtype = match &common {
                    Null => Type::optional(Int),
                    Int => Int,
                    Float => Float,
                    Optional(_) => common.clone(),
                    _ => unreachable!(
                        "valid numeric types are Int, Float, Optional[Int], Optional[Float]"
                    ),
                };
                // 3. Rewrite: use null if either side is null. Else,
                // cast to common type, do a division, and then snap to nearest
                // integral value
                let rewritten = match outtype {
                    Null => Expr::Cast {
                        expr: Box::new(Expr::Lit { value: Value::None }),
                        dtype: outtype.clone(),
                    },
                    _ => {
                        // if (div) {
                        //     *floordiv = floor(div);
                        //     if (div - *floordiv > 0.5) {
                        //         *floordiv += 1.0;
                        //     }
                        // }
                        todo!()
                    }
                };
                Ok(CompiledExpr {
                    rewritten,
                    original: self.clone(),
                    schema,
                    dtype: outtype,
                })
            }
            Expr::Binary { op, left, right } => {
                let left = left.compile(schema.clone())?;
                let right = right.compile(schema.clone())?;
                let ltype = left.dtype();
                let rtype = right.dtype();
                let (outtype, casttype) = match op {
                    BinOp::FloorDiv => unreachable!("handled separately"),
                    BinOp::Add | BinOp::Sub | BinOp::Mul | BinOp::Mod => {
                        // 1. Validate: both sides can be promoted to a numeric type
                        let max = Type::optional(Float);
                        if !promotable(ltype, &max) || !promotable(rtype, &max) {
                            bail!("invalid expression: both sides of '{}' must be numeric types but found {} & {}, left: {:?}, right: {:?}", op, ltype, rtype, left.original, right.original);
                        }

                        // 2. Find output type: either int, or float, or options
                        let outtype = match (ltype, rtype) {
                            (Null, Null) => Type::optional(Int),
                            // can unwrap because know both are numerics, so lca exists
                            (l, r) => lca(l, r).unwrap(),
                        };
                        (outtype.clone(), outtype)
                    }
                    BinOp::Div => {
                        // 1. Validate: both sides can be promoted to a numeric type
                        let max = Type::optional(Float);
                        if !promotable(ltype, &max) || !promotable(rtype, &max) {
                            bail!(
                                "invalid expression: both sides of '{}' must be numeric types but found {} & {}",
                                op,
                                ltype,
                                rtype
                            );
                        }
                        // can unwrap because we know both are numerics, so lca exists
                        let common = lca(ltype, rtype).unwrap();
                        // 2. Find output type: either a float or optional float
                        let outtype = match common {
                            Null | Optional(_) => Type::optional(Float),
                            _ => Float,
                        };
                        (outtype.clone(), outtype)
                    }
                    BinOp::Eq | BinOp::Neq => {
                        // 1. Validate: both sides can be promoted to a common type
                        let common = match lca(ltype, rtype) {
                            Some(t) => t,
                            None => bail!(
                                "invalid expression: both sides of '{}' must be of compatible types but found {} & {}",
                                op,
                                ltype,
                                rtype
                            ),
                        };
                        // 2. Find output type: either a boolean or optional boolean
                        let (casttype, outtype) = match &common {
                            Null => (Type::optional(Int), Type::optional(Bool)),
                            Optional(_) => (common, Type::optional(Bool)),
                            _ => (common, Bool),
                        };
                        (outtype, casttype)
                    }
                    BinOp::Gt | BinOp::Gte | BinOp::Lt | BinOp::Lte => {
                        // 1. Validate: both sides can be promoted to numeric types
                        let max = Type::optional(Float);
                        if !promotable(ltype, &max) || !promotable(rtype, &max) {
                            bail!(
                                "invalid expression: both sides of '{}' must be numeric types but found {} & {}",
                                op,
                                ltype,
                                rtype
                            );
                        }
                        // 2. Find output type: either a boolean or optional boolean
                        // can unwrap because we know both are numerics, so lca exists
                        let common = lca(ltype, rtype).unwrap();
                        let (casttype, outtype) = match &common {
                            Null => (Type::optional(Int), Type::optional(Bool)),
                            Optional(_) => (common, Type::optional(Bool)),
                            _ => (common, Bool),
                        };
                        (outtype, casttype)
                    }
                    BinOp::And | BinOp::Or => {
                        // 1. Validate: both sides can be promoted to a boolean
                        if !promotable(ltype, &Type::optional(Bool))
                            || !promotable(rtype, &Type::optional(Bool))
                        {
                            bail!(
                                "invalid expression: both sides of '{}' must be boolean types but found {} & {}",
                                op,
                                ltype,
                                rtype
                            );
                        }
                        // 2. Find output type: either a boolean or optional boolean
                        // can unwrap because we know both are booleans, so lca exists
                        let common = lca(ltype, rtype).unwrap();
                        let outtype = match common {
                            Null | Optional(_) => Type::optional(Bool),
                            _ => Bool,
                        };
                        (outtype.clone(), outtype)
                    }
                };
                let rewritten = match (ltype, rtype) {
                    (Null, Null) => Expr::Cast {
                        expr: Box::new(Expr::Lit { value: Value::None }),
                        dtype: outtype.clone(),
                    },
                    _ => Expr::Binary {
                        op: op.clone(),
                        left: Box::new(left.safecast(&casttype)?),
                        right: Box::new(right.safecast(&casttype)?),
                    },
                };
                Ok(CompiledExpr {
                    rewritten,
                    original: self.clone(),
                    schema,
                    dtype: outtype.clone(),
                })
            }
            Expr::Case {
                when_thens,
                otherwise,
            } => {
                if when_thens.is_empty() {
                    bail!("invalid expression: CASE must have at least one WHEN clause");
                }
                let mut cwts = vec![];
                for (when, then) in when_thens {
                    let cw = when.compile(schema.clone())?;
                    let ct = then.compile(schema.clone())?;
                    if !promotable(cw.dtype(), &Type::optional(Bool)) {
                        bail!(
                            "expected expression {:?} to be boolean for WHEN but found type {:?}",
                            when,
                            cw.dtype()
                        );
                    }
                    cwts.push((cw, ct));
                }
                // missing otherwise is allowed, in which case it is treated as None
                let otherwise = match otherwise {
                    None => Expr::Lit { value: Value::None },
                    Some(e) => e.as_ref().clone(),
                };
                let otherwise = otherwise.compile(schema.clone())?;

                // all then expressions + otherwise must be of compatible types
                let mut then_types = cwts.iter().map(|(_, t)| t.dtype()).collect_vec();
                then_types.push(&otherwise.dtype);
                // now starting with lca of first two, find lca of all
                let mut outtype = then_types[0].clone();
                for t in then_types.iter().skip(1) {
                    outtype = match lca(&outtype, t) {
                        Some(t) => t,
                        None => bail!("incompatible types in THEN expressions: {:?}", then_types),
                    };
                }
                let rewritten = match &outtype {
                    // if outtype is null, then all branches are null, just rewrite
                    Null => Expr::Lit { value: Value::None },
                    _ => {
                        // cast all whens to eval to bool and thens to eval to outtype
                        let mut rwts = vec![];
                        for (cw, ct) in cwts {
                            rwts.push((
                                cw.safecast(&Type::optional(Bool))?,
                                ct.safecast(&outtype)?,
                            ));
                        }
                        // rewrite the case expression
                        Expr::Case {
                            when_thens: rwts,
                            otherwise: Some(Box::new(otherwise.safecast(&outtype)?)),
                        }
                    }
                };
                Ok(CompiledExpr {
                    rewritten,
                    original: self.clone(),
                    schema,
                    dtype: outtype,
                })
            }
            Expr::IsNull { expr } => {
                let expr = expr.compile(schema.clone())?;
                Ok(CompiledExpr {
                    rewritten: Expr::IsNull {
                        expr: Box::new(expr.rewritten),
                    },
                    original: self.clone(),
                    schema,
                    dtype: Bool,
                })
            }
            Expr::FillNull { expr, default } => {
                let expr = expr.compile(schema.clone())?;
                let default = default.compile(schema.clone())?;
                // Validate: both sides can be promoted to a common type
                let outtype = match expr.dtype() {
                    Null => default.dtype().clone(),
                    _ => match lca(expr.dtype().inner(), default.dtype()) {
                        Some(t) => t,
                        None => bail!(
                            "invalid expression: both inputs of 'FILLNULL' must be of compatible types but found {} & {}",
                            expr.dtype(),
                            default.dtype()
                        ),
                    },
                };
                // Rewrite: use null if expr is null, casts otherwise
                let rewritten = match (expr.dtype(), &outtype) {
                    (_, Null) => Expr::Lit { value: Value::None },
                    // if expr is null, always use default
                    (Null, _) => default.rewritten.clone(),
                    _ => Expr::FillNull {
                        expr: Box::new(expr.safecast(&outtype)?),
                        default: Box::new(default.safecast(&outtype)?),
                    },
                };
                Ok(CompiledExpr {
                    rewritten,
                    original: self.clone(),
                    schema,
                    dtype: outtype,
                })
            }
            Expr::Cast { .. } => panic!("cast should not be exposed to the end user"),
        }
    }
}

#[derive(Copy, PartialEq, Clone, Serialize)]
pub enum MathFn {
    // number of decimal places, if None, round to nearest integer
    Round { precision: Option<i32> },
    Ceil,
    Floor,
    Abs,
}

impl std::fmt::Display for MathFn {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        match self {
            MathFn::Round { precision } => match precision {
                None => write!(f, "ROUND"),
                Some(p) => write!(f, "ROUND({})", p),
            },
            MathFn::Ceil => write!(f, "CEIL"),
            MathFn::Floor => write!(f, "FLOOR"),
            MathFn::Abs => write!(f, "ABS"),
        }
    }
}

#[derive(Copy, Clone, PartialEq, Serialize, Debug)]
pub enum UnOp {
    Neg,
    Not,
    Len, // length of a list, string, bytes, embedding, dict.
}

#[derive(Copy, Clone, PartialEq, Serialize, Debug)]
pub enum BinOp {
    Add,
    Sub,
    Mul,
    Div,
    Mod,
    FloorDiv,
    Eq,
    Neq,
    Gt,
    Gte,
    Lt,
    Lte,
    And,
    Or,
}

impl TryInto<ArrowLogicalExpr> for &CompiledExpr {
    type Error = anyhow::Error;
    fn try_into(self) -> Result<ArrowLogicalExpr> {
        let exp = &self.rewritten;
        Ok(exp.try_into()?)
    }
}

impl fmt::Display for CompiledExpr {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        write!(f, "{:?} -> {:?}", self.original, self.rewritten)
    }
}

fn adjust_index(index: &Expr) -> Expr {
    when(index.clone().lt(lit(0)), index.clone()).otherwise(index.clone().add(lit(1)))
}

impl TryInto<ArrowLogicalExpr> for &Expr {
    type Error = anyhow::Error;
    fn try_into(self) -> Result<ArrowLogicalExpr> {
        match self {
            Expr::Ref { name } => Ok(lexpr::col(name)),
            Expr::Lit { value } => Ok(datafusion_expr::lit(Into::<ScalarValue>::into(value))),
            Expr::Cast { expr, dtype } => Ok(lexpr::cast(
                expr.as_ref().try_into()?,
                to_arrow_dtype(dtype, false),
            )),
            Expr::ListFn { list, func } => {
                let list = list.as_ref().try_into()?;
                match func.as_ref() {
                    ListFn::Len => Ok(array_fn::array_length(list)),
                    ListFn::Get { index } => {
                        let index = adjust_index(index);
                        let index_lexpr = (&index).try_into()?;
                        Ok(array_fn::array_element(list, index_lexpr))
                    }
                    ListFn::Contains { item } => {
                        let item = item.try_into()?;
                        Ok(array_fn::array_has(list, item))
                    }
                    ListFn::HasNull => {
                        let none = datafusion_expr::lit(Into::<ScalarValue>::into(&Value::None));
                        Ok(array_fn::array_has(list, none))
                    }
                }
            }
            Expr::StringFn { func, expr } => {
                let expr = expr.as_ref().try_into()?;
                match func.as_ref() {
                    StringFn::Len => Ok(expr_fn::length(expr)),
                    StringFn::ToLower => Ok(expr_fn::lower(expr)),
                    StringFn::ToUpper => Ok(expr_fn::upper(expr)),
                    StringFn::Contains { key } => {
                        let key = key.try_into()?;
                        let zero = datafusion_expr::lit(0);
                        Ok(expr_fn::strpos(expr, key).not_eq(zero))
                    },
                    StringFn::StartsWith { key } => {
                        let key = key.try_into()?;
                        Ok(expr_fn::starts_with(expr, key))
                    },
                    StringFn::EndsWith { key } => {
                        let key = key.try_into()?;
                        Ok(expr_fn::ends_with(expr, key))
                    },
                    StringFn::Concat { other } => {
                        let other = other.try_into()?;
                        Ok(expr_fn::concat(vec![expr, other]))
                    }
                }
            }
            Expr::DictFn { .. } => todo!(),
            Expr::StructFn { struct_, func } => {
                let struct_ = struct_.as_ref().try_into()?;
                match func.as_ref() {
                    StructFn::Get { field } => {
                        let field = datafusion_expr::lit(Into::<ScalarValue>::into(
                            &Value::String(Arc::new(field.clone())),
                        ));
                        Ok(expr_fn::get_field(struct_, field))
                    }
                }
            }
            Expr::MathFn { func, expr } => {
                let expr: ArrowLogicalExpr = expr.as_ref().try_into()?;
                match func {
                    MathFn::Ceil => Ok(expr_fn::ceil(expr)),
                    MathFn::Floor => Ok(expr_fn::floor(expr)),
                    MathFn::Round { precision } => match precision {
                        None => Ok(expr_fn::round(vec![expr])),
                        Some(p) => Ok(expr_fn::round(vec![
                            expr,
                            datafusion_expr::lit(Into::<ScalarValue>::into(&Value::Int(*p as i64))),
                        ])),
                    },
                    MathFn::Abs => Ok(expr_fn::abs(expr)),
                }
            }
            Expr::Binary { op, left, right } => {
                let left = left.as_ref().try_into()?;
                let right = right.as_ref().try_into()?;
                Ok(lexpr::binary_expr(left, op.try_into()?, right))
            }
            Expr::Unary { op, expr } => match op {
                UnOp::Neg => Ok(lexpr::Expr::Negative(Box::new(expr.as_ref().try_into()?))),
                UnOp::Not => Ok(lexpr::not(expr.as_ref().try_into()?)),
                UnOp::Len => todo!(),
            },
            Expr::Case {
                when_thens,
                otherwise,
            } => {
                let first = when_thens.first().ok_or(anyhow!("empty when_thens"))?;
                let mut ret = lexpr::when((&first.0).try_into()?, (&first.1).try_into()?);
                for (when, then) in when_thens.iter().skip(1) {
                    ret.when(when.try_into()?, then.try_into()?);
                }
                match otherwise {
                    None => Ok(ret.end()?),
                    Some(otherwise) => Ok(ret.otherwise(otherwise.as_ref().try_into()?)?),
                }
            }
            Expr::FillNull { expr, default } => {
                let expr: lexpr::Expr = expr.as_ref().try_into()?;
                let default = default.as_ref().try_into()?;
                Ok(lexpr::when(lexpr::is_null(expr.clone()), default).otherwise(expr)?)
            }
            Expr::IsNull { expr } => Ok(lexpr::is_null(expr.as_ref().try_into()?)),
        }
    }
}

impl fmt::Display for Expr {
    // Display is same as Debug
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        write!(f, "{:?}", self)
    }
}

impl fmt::Debug for Expr {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        match self {
            Expr::Ref { name } => write!(f, "col({})", name),
            Expr::Lit { value } => write!(f, "lit({:?})", value),
            Expr::Cast { expr, dtype } => write!(f, "CAST({:?} AS {:?})", expr, dtype),
            Expr::Binary { op, left, right } => write!(f, "({:?} {} {:?})", left, op, right),
            Expr::Unary { op, expr } if matches!(op, UnOp::Len) => write!(f, "len({:?})", expr),
            Expr::Unary { op, expr } => write!(f, "({} {:?})", op, expr),
            Expr::Case {
                when_thens,
                otherwise,
            } => {
                // desired: CASE WHEN ... THEN ... WHEN ... THEN ... ELSE ...END
                let mut s = String::from("CASE ");
                for (when, then) in when_thens {
                    s.push_str(&format!("WHEN {{ {:?} }} THEN {{ {:?} }} ", when, then));
                }
                let end = match otherwise {
                    None => "END".to_string(),
                    Some(e) => format!("ELSE {{ {:?} }} END", e),
                };
                s.push_str(&end);
                write!(f, "{}", s)
            }
            Expr::IsNull { expr } => write!(f, "ISNULL({:?})", expr),
            Expr::FillNull { expr, default } => write!(f, "FILLNULL({:?}, {:?})", expr, default),
            Expr::MathFn { func, expr } => match func {
                MathFn::Ceil => write!(f, "{:?}.ceil()", expr),
                MathFn::Floor => write!(f, "{:?}.floor()", expr),
                MathFn::Round { precision } => {
                    if let Some(p) = precision {
                        write!(f, "{:?}.round({})", expr, p)
                    } else {
                        write!(f, "{:?}.round()", expr)
                    }
                }
                MathFn::Abs => write!(f, "{:?}.abs()", expr),
            },
            Expr::ListFn { list, func } => match func.as_ref() {
                ListFn::Len => write!(f, "{:?}.list.len()", list),
                ListFn::Get { index } => write!(f, "{:?}.list.get({:?})", list, index),
                ListFn::Contains { item: expr } => {
                    write!(f, "{:?}.list.contains({:?})", list, expr)
                }
                ListFn::HasNull => write!(f, "{:?}.list.has_null()", list),
            },
            Expr::DictFn { dict, func } => match func.as_ref() {
                DictFn::Len => write!(f, "{:?}.dict.len()", dict),
                DictFn::Get { key, default } => {
                    write!(f, "{:?}.dict.get({:?}, {:?})", dict, key, default)
                }
                DictFn::Contains { key } => write!(f, "{:?}.dict.contains({:?})", dict, key),
            },
            Expr::StructFn { struct_, func } => match func.as_ref() {
                StructFn::Get { field } => write!(f, "{:?}.{}", struct_, field),
            },
            Expr::StringFn { func, expr } => match func.as_ref() {
                StringFn::Len => write!(f, "{:?}.str.len()", expr),
                StringFn::ToLower => write!(f, "{:?}.str.lower()", expr),
                StringFn::ToUpper => write!(f, "{:?}.str.upper()", expr),
                StringFn::Contains { key } => write!(f, "{:?}.str.contains({:?})", expr, key),
                StringFn::StartsWith { key } => write!(f, "{:?}.str.starts_with({:?})", expr, key),
                StringFn::EndsWith { key } => write!(f, "{:?}.str.ends_with({:?})", expr, key),
                StringFn::Concat { other } => write!(f, "{:?}.str.concat({:?})", expr, other),
            },
        }
    }
}

impl fmt::Display for BinOp {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        match self {
            BinOp::Add => write!(f, "+"),
            BinOp::Sub => write!(f, "-"),
            BinOp::Mul => write!(f, "*"),
            BinOp::Div => write!(f, "/"),
            BinOp::Mod => write!(f, "%"),
            BinOp::Eq => write!(f, "=="),
            BinOp::Neq => write!(f, "!="),
            BinOp::Gt => write!(f, ">"),
            BinOp::Gte => write!(f, ">="),
            BinOp::Lt => write!(f, "<"),
            BinOp::Lte => write!(f, "<="),
            BinOp::And => write!(f, "and"),
            BinOp::Or => write!(f, "or"),
            BinOp::FloorDiv => write!(f, "//"),
        }
    }
}

impl TryInto<datafusion_expr::Operator> for &BinOp {
    type Error = anyhow::Error;
    fn try_into(self) -> Result<datafusion_expr::Operator> {
        use datafusion_expr::Operator;
        match self {
            BinOp::Add => Ok(Operator::Plus),
            BinOp::Sub => Ok(Operator::Minus),
            BinOp::Mul => Ok(Operator::Multiply),
            BinOp::Div => Ok(Operator::Divide),
            BinOp::Mod => Ok(Operator::Modulo),
            BinOp::Eq => Ok(Operator::Eq),
            BinOp::Neq => Ok(Operator::NotEq),
            BinOp::Gt => Ok(Operator::Gt),
            BinOp::Gte => Ok(Operator::GtEq),
            BinOp::Lt => Ok(Operator::Lt),
            BinOp::Lte => Ok(Operator::LtEq),
            BinOp::And => Ok(Operator::And),
            BinOp::Or => Ok(Operator::Or),
            BinOp::FloorDiv => bail!("floor division not supported"),
        }
    }
}

impl fmt::Display for UnOp {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        match self {
            UnOp::Neg => write!(f, "-"),
            UnOp::Not => write!(f, "!"),
            UnOp::Len => write!(f, "LEN"),
        }
    }
}

impl Into<ScalarValue> for &Value {
    fn into(self) -> ScalarValue {
        match self {
            Value::None => ScalarValue::Null,
            Value::Int(v) => ScalarValue::Int64(Some(*v)),
            Value::Float(v) => ScalarValue::Float64(Some(*v)),
            Value::Bool(v) => ScalarValue::Boolean(Some(*v)),
            Value::String(v) => ScalarValue::Utf8(Some(v.as_ref().to_owned())),
            Value::Bytes(v) => ScalarValue::Binary(Some(v.as_ref().to_owned())),
            Value::Timestamp(v) => {
                ScalarValue::TimestampMicrosecond(Some(v.micros()), Some("+00:00".into()))
            }
            Value::Struct(v) => {
                let mut fields = vec![];
                let mut arrays = vec![];
                for (name, value) in v.fields() {
                    let dtype = natural_type(value);
                    let f = Field::new(name.clone(), dtype);
                    fields.push(to_arrow_field(&f));
                    // also convert the value to an array
                    // unwrap is safe we can allocate an array of size 1
                    let sv: ScalarValue = value.into();
                    arrays.push(sv.to_array().unwrap());
                }
                let arr = arrow::array::StructArray::new(fields.into(), arrays, None);
                ScalarValue::Struct(Arc::new(arr))
            }

            // Embedding(Arc<Vec<f64>>),
            // Struct(Arc<Struct>),
            // Decimal(Arc<Decimal>),
            // Date(Date),
            _ => todo!(),
        }
    }
}

fn none_as(dtype: &Type) -> Expr {
    Expr::Cast {
        expr: Box::new(Expr::Lit { value: Value::None }),
        dtype: dtype.clone(),
    }
}

/// Given a value, return the simplest natural type that can hold it
/// returning None for Value::None
fn natural_type(value: &Value) -> Type {
    match value {
        Value::None => Type::Null,
        Value::Int(_) => Type::Int,
        Value::Float(_) => Type::Float,
        Value::Bool(_) => Type::Bool,
        Value::String(_) => Type::String,
        Value::Bytes(_) => Type::Bytes,
        Value::Timestamp(_) => Type::Timestamp,
        Value::Embedding(e) => Type::Embedding(e.len()),
        Value::Struct(s) => {
            let fields = s
                .fields()
                .map(|(n, v)| Field::new(n.clone(), natural_type(v)))
                .collect();
            Type::Struct(Box::new(
                StructType::new("anon".into(), fields).unwrap(),
            ))
        }
        Value::Decimal(v) => Type::Decimal(DecimalType::new(v.scale()).unwrap()),
        Value::Date(_) => Type::Date,
        Value::List(l) => Type::List(Box::new(l.dtype().clone())),
        Value::Map(m) => Type::Map(Box::new(m.dtype().clone())),
    }
}
pub mod builders {
    use super::*;

    pub fn lit(x: impl Into<Value>) -> Expr {
        Expr::Lit { value: x.into() }
    }

    pub fn floor(e: Expr) -> Expr {
        Expr::MathFn {
            func: MathFn::Floor,
            expr: Box::new(e),
        }
    }

    pub fn ceil(e: Expr) -> Expr {
        Expr::MathFn {
            func: MathFn::Ceil,
            expr: Box::new(e),
        }
    }

    pub fn roundto(e: Expr, precision: i32) -> Expr {
        Expr::MathFn {
            func: MathFn::Round {
                precision: Some(precision),
            },
            expr: Box::new(e),
        }
    }

    pub fn round(e: Expr) -> Expr {
        Expr::MathFn {
            func: MathFn::Round { precision: None },
            expr: Box::new(e),
        }
    }

    pub fn abs(e: Expr) -> Expr {
        Expr::MathFn {
            func: MathFn::Abs,
            expr: Box::new(e),
        }
    }

    pub fn col(name: &str) -> Expr {
        Expr::Ref {
            name: name.to_string(),
        }
    }

    pub fn isnull(expr: Expr) -> Expr {
        Expr::IsNull {
            expr: Box::new(expr),
        }
    }

    pub fn fillnull(expr: Expr, default: Expr) -> Expr {
        Expr::FillNull {
            expr: Box::new(expr),
            default: Box::new(default),
        }
    }

    pub fn binary(left: impl Into<Box<Expr>>, op: BinOp, right: impl Into<Box<Expr>>) -> Expr {
        Expr::Binary {
            op,
            left: left.into(),
            right: right.into(),
        }
    }

    pub fn cast(expr: Expr, dtype: Type) -> Expr {
        Expr::Cast {
            expr: Box::new(expr),
            dtype,
        }
    }

    pub fn unary(op: UnOp, expr: Expr) -> Expr {
        Expr::Unary {
            op,
            expr: Box::new(expr),
        }
    }

    pub fn not(expr: Expr) -> Expr {
        unary(UnOp::Not, expr)
    }

    pub fn neg(expr: Expr) -> Expr {
        unary(UnOp::Neg, expr)
    }

    impl Expr {
        pub fn dot(self, field: &str) -> Expr {
            Expr::StructFn {
                struct_: Box::new(self),
                func: Box::new(StructFn::Get {
                    field: field.to_string(),
                }),
            }
        }
        pub fn str_len(self) -> Expr {
            Expr::StringFn {
                expr: Box::new(self),
                func: Box::new(StringFn::Len),
            }
        }
        pub fn str_to_upper(self) -> Expr {
            Expr::StringFn {
                expr: Box::new(self),
                func: Box::new(StringFn::ToUpper),
            }
        }
        pub fn str_to_lower(self) -> Expr {
            Expr::StringFn {
                expr: Box::new(self),
                func: Box::new(StringFn::ToLower),
            }
        }
        pub fn str_contains(self, key: Expr) -> Expr {
            Expr::StringFn {
                expr: Box::new(self),
                func: Box::new(StringFn::Contains { key })
            }
        }
        pub fn str_starts_with(self, key: Expr) -> Expr {
            Expr::StringFn {
                expr: Box::new(self),
                func: Box::new(StringFn::StartsWith { key })
            }
        }
        pub fn str_ends_with(self, key: Expr) -> Expr {
            Expr::StringFn {
                expr: Box::new(self),
                func: Box::new(StringFn::EndsWith { key })
            }
        }
        pub fn str_concat(self, other: Expr) -> Expr {
            Expr::StringFn {
                expr: Box::new(self),
                func: Box::new(StringFn::Concat { other })
            }
        }
        pub fn list_at(self, index: Expr) -> Expr {
            Expr::ListFn {
                list: Box::new(self),
                func: Box::new(ListFn::Get { index }),
            }
        }
        pub fn list_len(self) -> Expr {
            Expr::ListFn {
                list: Box::new(self),
                func: Box::new(ListFn::Len),
            }
        }
        pub fn list_has(self, item: Expr) -> Expr {
            Expr::ListFn {
                list: Box::new(self),
                func: Box::new(ListFn::Contains { item }),
            }
        }
        pub fn list_has_null(self) -> Expr {
            Expr::ListFn {
                list: Box::new(self),
                func: Box::new(ListFn::HasNull),
            }
        }

        pub fn and(self, other: Expr) -> Expr {
            binary(Box::new(self), BinOp::And, Box::new(other))
        }
        pub fn or(self, other: Expr) -> Expr {
            binary(Box::new(self), BinOp::Or, Box::new(other))
        }
        pub fn sub(self, other: Expr) -> Expr {
            binary(Box::new(self), BinOp::Sub, Box::new(other))
        }
        pub fn add(self, other: Expr) -> Expr {
            binary(Box::new(self), BinOp::Add, Box::new(other))
        }
        pub fn mul(self, other: Expr) -> Expr {
            binary(Box::new(self), BinOp::Mul, Box::new(other))
        }
        pub fn div(self, other: Expr) -> Expr {
            binary(Box::new(self), BinOp::Div, Box::new(other))
        }
        pub fn eq(self, other: Expr) -> Expr {
            binary(Box::new(self), BinOp::Eq, Box::new(other))
        }
        pub fn neq(self, other: Expr) -> Expr {
            binary(Box::new(self), BinOp::Neq, Box::new(other))
        }
        pub fn gt(self, other: Expr) -> Expr {
            binary(Box::new(self), BinOp::Gt, Box::new(other))
        }
        pub fn gte(self, other: Expr) -> Expr {
            binary(Box::new(self), BinOp::Gte, Box::new(other))
        }
        pub fn lt(self, other: Expr) -> Expr {
            binary(Box::new(self), BinOp::Lt, Box::new(other))
        }
        pub fn lte(self, other: Expr) -> Expr {
            binary(Box::new(self), BinOp::Lte, Box::new(other))
        }
        pub fn when(self, expr: Expr, then: Expr) -> Expr {
            match self {
                Expr::Case {
                    when_thens,
                    otherwise,
                } => {
                    let mut when_thens = when_thens;
                    when_thens.push((expr, then));
                    Expr::Case {
                        when_thens,
                        otherwise,
                    }
                }
                _ => panic!("expected CASE expression"),
            }
        }
        pub fn otherwise(self, expr: Expr) -> Expr {
            match self {
                Expr::Case {
                    when_thens,
                    otherwise: None,
                } => Expr::Case {
                    when_thens,
                    otherwise: Some(Box::new(expr)),
                },
                _ => panic!("expected CASE expression"),
            }
        }
    }
    pub fn when(expr: Expr, then: Expr) -> Expr {
        Expr::Case {
            when_thens: vec![(expr, then)],
            otherwise: None,
        }
    }
    impl std::ops::Mul<Expr> for Expr {
        type Output = Expr;

        fn mul(self, rhs: Expr) -> Expr {
            self.mul(rhs)
        }
    }

    impl std::ops::Div<Expr> for Expr {
        type Output = Expr;

        fn div(self, rhs: Expr) -> Expr {
            self.div(rhs)
        }
    }

    impl std::ops::Add<Expr> for Expr {
        type Output = Expr;

        fn add(self, rhs: Expr) -> Expr {
            self.add(rhs)
        }
    }
    impl std::ops::Sub<Expr> for Expr {
        type Output = Expr;

        fn sub(self, rhs: Expr) -> Expr {
            self.sub(rhs)
        }
    }
}

/// Proto conversion code

impl TryFrom<&ProtoExpr> for Expr {
    type Error = anyhow::Error;

    fn try_from(value: &ProtoExpr) -> std::result::Result<Self, Self::Error> {
        value.clone().try_into()
    }
}


impl TryFrom<ProtoExpr> for Expr {
    type Error = anyhow::Error;

    fn try_from(value: ProtoExpr) -> Result<Self> {
        let expr = match value.node {
            Some(eproto::expr::Node::Ref(r)) => Expr::Ref { name: r.name },
            Some(eproto::expr::Node::JsonLiteral(l)) =>{
                let dtype = l.dtype.ok_or(anyhow!("missing json literal dtype"))?.try_into()?;
                Expr::Lit { value: Value::from_json(&dtype, &l.literal)? }
            },
            Some(eproto::expr::Node::Binary(b)) => Expr::Binary {
                op: b.op.try_into()?,
                left: Box::new(b.left.ok_or(anyhow!("missing binary left"))?.as_ref().try_into()?),
                right: Box::new(b.right.ok_or(anyhow!("missing binary right"))?.as_ref().try_into()?),
            },
            Some(eproto::expr::Node::Unary(u)) => Expr::Unary {
                op: u.op.try_into()?,
                expr: Box::new(u.operand.ok_or(anyhow!("missing unary operand"))?.as_ref().try_into()?),
            },
            Some(eproto::expr::Node::MathFn(m)) => {
                if m.r#fn.is_none() {
                    bail!("missing mathfn func");
                }
                Expr::MathFn {
                    func: match m.r#fn.unwrap().fn_type {
                        Some(eproto::math_op::FnType::Abs(_)) => MathFn::Abs, 
                        Some(eproto::math_op::FnType::Ceil(_)) => MathFn::Ceil,
                        Some(eproto::math_op::FnType::Floor(_)) => MathFn::Floor,
                        Some(eproto::math_op::FnType::Round(r)) => MathFn::Round {
                            precision: Some(r.precision),
                        },
                        None => bail!("missing mathfn func"),
                    },
                    expr: Box::new(m.operand.ok_or(anyhow!("missing mathfn operand"))?.as_ref().try_into()?),
                }
            },
            Some(eproto::expr::Node::StringFn(s)) => {
                if s.r#fn.is_none() {
                    bail!("missing stringfn func");
                }
                Expr::StringFn {
                func: match s.r#fn.unwrap().fn_type {
                    Some(eproto::string_op::FnType::Len(_)) => Box::new(StringFn::Len),
                    Some(eproto::string_op::FnType::Tolower(_)) => Box::new(StringFn::ToLower),
                    Some(eproto::string_op::FnType::Toupper(_)) => Box::new(StringFn::ToUpper),
                    Some(eproto::string_op::FnType::Contains(c)) => Box::new(StringFn::Contains {
                        key: c.element.ok_or(anyhow!("missing contains key"))?.as_ref().try_into()?,
                    }),
                    Some(eproto::string_op::FnType::Startswith(c)) => Box::new(StringFn::StartsWith {
                        key: c.key.ok_or(anyhow!("missing startswith key"))?.as_ref().try_into()?,
                    }),
                    Some(eproto::string_op::FnType::Endswith(c)) => Box::new(StringFn::EndsWith {
                        key: c.key.ok_or(anyhow!("missing endswith key"))?.as_ref().try_into()?,
                    }),
                    Some(eproto::string_op::FnType::Concat(c)) => Box::new(StringFn::Concat {
                        other: c.other.ok_or(anyhow!("missing concat other"))?.as_ref().try_into()?,
                    }),
                    None => bail!("missing stringfn func"),
                },
                expr: Box::new(s.string.ok_or(anyhow!("missing stringfn expr"))?.as_ref().try_into()?),
                }
            },
            Some(eproto::expr::Node::DictFn(d)) => { 
                    if d.r#fn.is_none() {
                        bail!("missing dictfn func");
                    }

                    Expr::DictFn {
                    dict: Box::new(d.dict.ok_or(anyhow!("missing dictfn dict"))?.as_ref().try_into()?),
                    func: match d.r#fn.unwrap().fn_type {
                        Some(eproto::dict_op::FnType::Len(_)) => Box::new(DictFn::Len),
                        Some(eproto::dict_op::FnType::Get(g)) => {
                            if g.field.is_none() {
                                bail!("missing dictfn get field in dictfn");
                            }
                       
                            Box::new(DictFn::Get {
                                key: g.field.unwrap().as_ref().try_into()?,
                                default: g.default_value.map(|x| x.as_ref().try_into()).transpose()?,
                            })
                        },
                        Some(eproto::dict_op::FnType::Contains(c)) => Box::new(DictFn::Contains {
                            key: c.element.ok_or(anyhow!("missing dictfn contains key"))?.as_ref().try_into()?,
                        }),
                        None => bail!("missing dictfn func"),
                    },
                }
            },
            Some(eproto::expr::Node::StructFn(s)) => {
                    if s.r#fn.is_none() {
                        bail!("missing structfn func");
                    }

                    Expr::StructFn {
                    struct_: Box::new(s.r#struct.ok_or(anyhow!("missing structfn struct"))?.as_ref().try_into()?),
                    func: match s.r#fn.unwrap().fn_type {
                        Some(eproto::struct_op::FnType::Field(field)) => Box::new(StructFn::Get {field }),
                        None => bail!("missing structfn func"),
                    },
                }
            },
            Some(eproto::expr::Node::ListFn(l)) => {
                    if l.r#fn.is_none() {
                        bail!("missing listfn func");
                    }

                    Expr::ListFn {
                    list: Box::new(l.list.ok_or(anyhow!("missing listfn list"))?.as_ref().try_into()?),
                    func: match l.r#fn.unwrap().fn_type {
                        Some(eproto::list_op::FnType::Len(_)) => Box::new(ListFn::Len),
                        Some(eproto::list_op::FnType::Get(index)) => Box::new(ListFn::Get {
                            index: index.as_ref().try_into()?,
                        }),
                        Some(eproto::list_op::FnType::Contains(c)) => Box::new(ListFn::Contains {
                            item: c.element.ok_or(anyhow!("missing listfn contains item"))?.as_ref().try_into()?,
                        }),
                        None => bail!("missing listfn func"),
                    },
                }
            },
            Some(eproto::expr::Node::Case(c)) => {
                let mut when_thens = vec![];
                for w in c.when_then {
                    when_thens.push((
                        w.when.ok_or(anyhow!("missing case when"))?.try_into()?,
                        w.then.ok_or(anyhow!("missing case then"))?.try_into()?,
                    ));
                }
                Expr::Case {
                    when_thens,
                    otherwise: match c.otherwise {
                            None => None,
                            Some(o) => Some(Box::new(o.as_ref().try_into()?)),
                    }
                }
            }
            Some(eproto::expr::Node::Isnull(i)) => Expr::IsNull {
                expr: Box::new(i.operand.ok_or(anyhow!("missing isnull expr"))?.as_ref().try_into()?),
            },
            Some(eproto::expr::Node::Fillnull(f)) => Expr::FillNull {
                expr: Box::new(f.operand.ok_or(anyhow!("missing fillnull expr"))?.as_ref().try_into()?),
                default: Box::new(f.fill.ok_or(anyhow!("missing fillnull default"))?.as_ref().try_into()?),
            },
            None => bail!("missing expr node"),
        };
        Ok(expr)
    }
}


impl TryFrom<i32> for BinOp {
    type Error = anyhow::Error;

    fn try_from(value: i32) -> Result<Self> {
        match value {
            x if x == crate::schema_proto::expr::BinOp::Add as i32 => Ok(BinOp::Add),
            x if x == crate::schema_proto::expr::BinOp::Sub as i32 => Ok(BinOp::Sub),
            x if x== crate::schema_proto::expr::BinOp::Mul as i32 => Ok(BinOp::Mul),
            x if x == crate::schema_proto::expr::BinOp::Div as i32 => Ok(BinOp::Div),
            x if x == crate::schema_proto::expr::BinOp::Mod as i32 => Ok(BinOp::Mod),
            x if x == crate::schema_proto::expr::BinOp::FloorDiv as i32 => Ok(BinOp::FloorDiv),
            x if x == crate::schema_proto::expr::BinOp::Eq as i32 => Ok(BinOp::Eq),
            x if x == crate::schema_proto::expr::BinOp::Ne as i32 => Ok(BinOp::Neq),
            x if x == crate::schema_proto::expr::BinOp::Gt as i32 => Ok(BinOp::Gt),
            x if x == crate::schema_proto::expr::BinOp::Gte as i32 => Ok(BinOp::Gte),
            x if x == crate::schema_proto::expr::BinOp::Lt as i32 => Ok(BinOp::Lt),
            x if x == crate::schema_proto::expr::BinOp::Lte as i32 => Ok(BinOp::Lte),
            x if x == crate::schema_proto::expr::BinOp::And as i32 => Ok(BinOp::And),
            x if x == crate::schema_proto::expr::BinOp::Or as i32 => Ok(BinOp::Or),
            _ => bail!("invalid binop"),
        }
    }
}

impl TryFrom<i32> for UnOp {
    type Error = anyhow::Error;

    fn try_from(value: i32) -> Result<Self> {
        match value {
            x if x == crate::schema_proto::expr::UnaryOp::Neg as i32 => Ok(UnOp::Neg),
            x if x == crate::schema_proto::expr::UnaryOp::Not as i32 => Ok(UnOp::Not),
            x if x == crate::schema_proto::expr::UnaryOp::Len as i32 => Ok(UnOp::Len),
            _ => bail!("invalid unop"),
        }
    }
}

impl From<Expr> for ProtoExpr {
    fn from(expr: Expr) -> Self {
        let node = match expr {
            Expr::Ref { name } => Some(eproto::expr::Node::Ref(eproto::Ref { name })),
            Expr::Lit { value } => {
                let literal = value.to_json(); 
                let dtype = natural_type(&value);
                Some(eproto::expr::Node::JsonLiteral(eproto::JsonLiteral {
                    literal: literal.to_string(),
                    dtype: Some((&dtype).into()),
                }))
            },
            Expr::Unary { op, expr } => Some(eproto::expr::Node::Unary(Box::new(eproto::Unary {
                op: op.into(),
                operand: Some(Box::new((*expr).into())),
            }))),
            Expr::Binary { op, left, right } => Some(eproto::expr::Node::Binary(Box::new(eproto::Binary {
                op: op.into(),
                left: Some(Box::new((*left).into())),
                right: Some(Box::new((*right).into())),
            }))),
            Expr::Case { when_thens, otherwise } => Some(eproto::expr::Node::Case(Box::new(eproto::Case {
                when_then: when_thens.into_iter().map(|(when, then)| eproto::WhenThen {
                    when: Some(when.into()),
                    then: Some(then.into()),
                }).collect::<Vec<_>>(),
                otherwise: otherwise
                    .map(|o| Box::new((*o).into()))
            }))),
            Expr::IsNull { expr } => Some(eproto::expr::Node::Isnull(Box::new(eproto::IsNull {
                operand: Some(Box::new((*expr).into())),
            }))),
            Expr::FillNull { expr, default } => Some(eproto::expr::Node::Fillnull(Box::new(eproto::FillNull {
                operand: Some(Box::new((*expr).into())),
                fill: Some(Box::new((*default).into())),
            }))),
            Expr::MathFn { func, expr } => {
                let math_fn = match func {
                    MathFn::Abs => eproto::MathOp { fn_type: Some(eproto::math_op::FnType::Abs(eproto::Abs {})) },
                    MathFn::Ceil => eproto::MathOp { fn_type: Some(eproto::math_op::FnType::Ceil(eproto::Ceil {})) },
                    MathFn::Floor => eproto::MathOp { fn_type: Some(eproto::math_op::FnType::Floor(eproto::Floor {})) },
                    MathFn::Round { precision } => eproto::MathOp {
                        fn_type: Some(eproto::math_op::FnType::Round(eproto::Round { precision: precision.unwrap_or(0) })),
                    },
                };
                Some(eproto::expr::Node::MathFn(Box::new(eproto::MathFn {
                    operand: Some(Box::new((*expr).into())),
                    r#fn: Some(math_fn),
                })))
            },
            Expr::StringFn { func, expr } => {
                let string_fn = match *func {
                    StringFn::Len => eproto::StringOp { fn_type: Some(eproto::string_op::FnType::Len(eproto::Len {})) },
                    StringFn::ToLower => eproto::StringOp { fn_type: Some(eproto::string_op::FnType::Tolower(eproto::ToLower {})) },
                    StringFn::ToUpper => eproto::StringOp { fn_type: Some(eproto::string_op::FnType::Toupper(eproto::ToUpper {})) },
                    StringFn::Contains { ref key } => eproto::StringOp {
                        fn_type: Some(eproto::string_op::FnType::Contains(Box::new(eproto::Contains {
                            element: Some(Box::new(key.clone().into())),
                        }))),
                    },
                    StringFn::StartsWith { ref key } => eproto::StringOp {
                        fn_type: Some(eproto::string_op::FnType::Startswith(Box::new(eproto::StartsWith {
                            key: Some(Box::new(key.clone().into())),
                        }))),
                    },
                    StringFn::EndsWith { ref key } => eproto::StringOp {
                        fn_type: Some(eproto::string_op::FnType::Endswith(Box::new(eproto::EndsWith {
                            key: Some(Box::new(key.clone().into())),
                        }))),
                    },
                    StringFn::Concat { ref other } => eproto::StringOp {
                        fn_type: Some(eproto::string_op::FnType::Concat(Box::new(eproto::Concat {
                            other: Some(Box::new(other.clone().into())),
                        }))),
                    },
                };
                Some(eproto::expr::Node::StringFn(Box::new(eproto::StringFn {
                    string: Some(Box::new((*expr).into())),
                    r#fn: Some(Box::new(string_fn)),
                })))
            },
            Expr::DictFn { dict, func } => {
                let dict_fn = match *func {
                    DictFn::Len => eproto::DictOp { fn_type: Some(eproto::dict_op::FnType::Len(eproto::Len {})) },
                    DictFn::Contains { ref key } => eproto::DictOp {
                        fn_type: Some(eproto::dict_op::FnType::Contains(Box::new(eproto::Contains {
                            element: Some(Box::new(key.clone().into())),
                        }))),
                    },
                    DictFn::Get { ref key, ref default } => {
                        let default_value = match default.clone() {
                            Some(d) => Some(Box::new(d.into())),
                            None => None,
                        };
            
                        eproto::DictOp {
                            fn_type: Some(eproto::dict_op::FnType::Get(Box::new(eproto::DictGet {
                                field: Some(Box::new(key.clone().into())),
                                default_value,
                            }))),
                        }
                    }
                };
                Some(eproto::expr::Node::DictFn(Box::new(eproto::DictFn {
                    dict: Some(Box::new((*dict).into())),
                    r#fn: Some(Box::new(dict_fn)),
                })))
            },
            Expr::StructFn { struct_, func } => {
                let struct_fn = match *func {
                    StructFn::Get { ref field } => eproto::StructOp { fn_type: Some(eproto::struct_op::FnType::Field(field.clone())) },
                };
                Some(eproto::expr::Node::StructFn(Box::new(eproto::StructFn {
                    r#struct: Some(Box::new((*struct_).into())),
                    r#fn: Some(struct_fn),
                })))
            },
            Expr::ListFn { list, func } => {
                let list_fn = match *func {
                    ListFn::Len => eproto::ListOp { fn_type: Some(eproto::list_op::FnType::Len(eproto::Len {})) },
                    ListFn::Contains { ref item } => eproto::ListOp {
                        fn_type: Some(eproto::list_op::FnType::Contains(Box::new(eproto::Contains {
                            element: Some(Box::new(item.clone().into())),
                        }))),
                    },
                    ListFn::Get { ref index } => eproto::ListOp {
                        fn_type: Some(eproto::list_op::FnType::Get(Box::new(index.clone().into()))),
                    },
                    ListFn::HasNull => unimplemented!("list has null is not yet implemented"), 
                };
                Some(eproto::expr::Node::ListFn(Box::new(eproto::ListFn {
                    list: Some(Box::new((*list).into())),
                    r#fn: Some(Box::new(list_fn)),
                })))
            },
            Expr::Cast { ..} => panic!("Cast should not be serialized"), 
        };
        ProtoExpr { node }
    }
}


// Conversion for BinOp
impl From<BinOp> for i32 {
    fn from(op: BinOp) -> Self {
        match op {
            BinOp::Add => crate::schema_proto::expr::BinOp::Add as i32,
            BinOp::Sub => crate::schema_proto::expr::BinOp::Sub as i32,
            BinOp::Mul => crate::schema_proto::expr::BinOp::Mul as i32,
            BinOp::Div => crate::schema_proto::expr::BinOp::Div as i32,
            BinOp::Mod => crate::schema_proto::expr::BinOp::Mod as i32,
            BinOp::FloorDiv => crate::schema_proto::expr::BinOp::FloorDiv as i32,
            BinOp::Eq => crate::schema_proto::expr::BinOp::Eq as i32,
            BinOp::Neq => crate::schema_proto::expr::BinOp::Ne as i32,
            BinOp::Gt => crate::schema_proto::expr::BinOp::Gt as i32,
            BinOp::Gte => crate::schema_proto::expr::BinOp::Gte as i32,
            BinOp::Lt => crate::schema_proto::expr::BinOp::Lt as i32,
            BinOp::Lte => crate::schema_proto::expr::BinOp::Lte as i32,
            BinOp::And => crate::schema_proto::expr::BinOp::And as i32,
            BinOp::Or => crate::schema_proto::expr::BinOp::Or as i32,
        }
    }
}

// Conversion for UnOp
impl From<UnOp> for i32 {
    fn from(op: UnOp) -> Self {
        match op {
            UnOp::Neg => crate::schema_proto::expr::UnaryOp::Neg as i32,
            UnOp::Not => crate::schema_proto::expr::UnaryOp::Not as i32,
            UnOp::Len => crate::schema_proto::expr::UnaryOp::Len as i32,
        }
    }
}


#[cfg(test)]
mod tests {

    use super::builders::*;
    use super::*;
    use crate::df::Dataframe;
    use crate::rowcol::Col;
    use crate::schema::Field;
    use itertools::Itertools;
    use std::sync::Arc;
    use Type::*;
    use crate::value;
    use crate::types;
    use crate::value::Value;

    #[derive(Debug, Clone)]
    struct Case {
        expr: Expr,
        valid: Option<bool>,
        matches: Vec<(Type, Vec<Value>)>,
        mismatches: Vec<Type>,
        produces: Option<(Type, Vec<Value>)>,
    }

    fn check(df: Dataframe, cases: impl IntoIterator<Item = Case>) {
        for case in cases {
            // first verify that case itself is well formed
            case.check();
            let schema = df.schema();
            let compiled = case.expr.compile(schema.clone());
            match case.valid {
                None => panic!("invalid test case: validity not set"),
                Some(false) => {
                    assert!(compiled.is_err(), "expected {:?} to be invalid", case.expr);
                    continue;
                }
                Some(true) => {
                    let compiled = compiled.unwrap();
                    // verify all mismatches
                    for dtype in &case.mismatches {
                        assert!(
                            !compiled.matches(dtype),
                            "expected {:?} to not match for expr: {} of type {:?}",
                            dtype,
                            compiled,
                            compiled.dtype()
                        );
                    }
                    // if matches is set, verify that it matches
                    for (dtype, expected) in &case.matches {
                        assert!(
                            compiled.matches(dtype),
                            "expected {:?} to match for expr: {} of type {:?}",
                            dtype,
                            compiled,
                            compiled.dtype()
                        );
                        let found = df.eval(&compiled, dtype.clone(), "result").unwrap();
                        let expected = Col::from("result", dtype.clone(), expected.clone());
                        assert!(
                            expected.is_ok(),
                            "could not create col for expr: {}, error: {:?}",
                            compiled,
                            expected
                        );
                        assert_eq!(found, expected.unwrap(), "mismatch for expr: {}", compiled);
                    }
                    // if produces is set, verify that it produces
                    if let Some((dtype, expected)) = &case.produces {
                        assert!(
                            compiled.dtype() == dtype,
                            "expression {}, expected to produce type {:?} but got {:?}",
                            compiled,
                            dtype,
                            compiled.dtype()
                        );
                        let expected = Col::from("result", dtype.clone(), expected.clone());
                        let found = df.eval(&compiled, dtype.clone(), "result");
                        assert!(
                            found.is_ok(),
                            "could not eval expr: {}, error: {:?}",
                            compiled,
                            found.unwrap_err()
                        );
                        assert_eq!(
                            found.unwrap(),
                            expected.unwrap(),
                            "mismatch for expr: {}",
                            compiled
                        );
                    }
                }
            }
        }
    }
    impl Case {
        fn new(expr: Expr) -> Self {
            Self {
                expr,
                valid: None,
                mismatches: vec![],
                matches: vec![],
                produces: None,
            }
        }
        fn invalid(mut self) -> Self {
            self.valid = Some(false);
            self
        }
        fn produces<T: Into<Value>>(
            mut self,
            dtype: Type,
            values: impl IntoIterator<Item = T>,
        ) -> Self {
            self.valid = Some(true);
            self.produces = Some((dtype, values.into_iter().map(Into::into).collect()));
            self
        }
        fn matches<T: Into<Value>>(
            mut self,
            dtype: Type,
            values: impl IntoIterator<Item = T>,
        ) -> Self {
            self.valid = Some(true);
            let expected =
                Col::from("result", dtype.clone(), values.into_iter().map(Into::into)).unwrap();
            let expected = expected.values().to_vec();
            self.matches.push((dtype, expected));
            self
        }

        fn mismatches(mut self, dtypes: impl IntoIterator<Item = Type>) -> Self {
            self.mismatches.extend(dtypes);
            self
        }

        fn check(&self) {
            // case is well formed: either it's invalid or it has matches
            if self.valid.is_none() {
                assert!(!self.matches.is_empty(), "no matches set");
            }
        }
    }

    fn list_df() -> Dataframe {
        // create customer df - with one list of int column, one optional list
        // of int, one list of optional int, and one non-list int column
        let ltype1 = List(Box::new(Int));
        let ltype2 = Type::optional(ltype1.clone());
        let ltype3 = List(Box::new(Type::optional(Int)));
        let ltype4 = Type::optional(List(Box::new(Float)));
        let ltype5 = Type::optional(List(Box::new(Type::optional(Int))));
        let df = Dataframe::new(vec![
            Col::new(
                Arc::new(Field::new("a", ltype1.clone())),
                Arc::new(vec![
                    Value::List(Arc::new(
                        value::List::new(Int, &[Value::Int(1), Value::Int(2)]).unwrap(),
                    )),
                    Value::List(Arc::new(value::List::new(Int, &[Value::Int(3)]).unwrap())),
                    Value::List(Arc::new(
                        value::List::new(Int, &[Value::Int(4), Value::Int(5)]).unwrap(),
                    )),
                ]),
            )
            .unwrap(),
            Col::new(
                Arc::new(Field::new("b", ltype2.clone())),
                Arc::new(vec![
                    Value::List(Arc::new(
                        value::List::new(Int, &[Value::Int(1), Value::Int(2)]).unwrap(),
                    )),
                    Value::None,
                    Value::List(Arc::new(
                        value::List::new(Int, &[Value::Int(4), Value::Int(5)]).unwrap(),
                    )),
                ]),
            )
            .unwrap(),
            Col::new(
                Arc::new(Field::new("c", ltype3.clone())),
                Arc::new(vec![
                    Value::List(Arc::new(
                        value::List::new(
                            Type::optional(Int),
                            &[Value::Int(1), Value::None, Value::Int(2)],
                        )
                        .unwrap(),
                    )),
                    Value::List(Arc::new(
                        value::List::new(
                            Type::optional(Int),
                            &[Value::Int(11), Value::Int(4), Value::Int(2)],
                        )
                        .unwrap(),
                    )),
                    Value::List(Arc::new(
                        value::List::new(
                            Type::optional(Int),
                            &[Value::Int(3), Value::None, Value::Int(6)],
                        )
                        .unwrap(),
                    )),
                ]),
            )
            .unwrap(),
            Col::new(
                Arc::new(Field::new("d", Int)),
                Arc::new(vec![Value::Int(0), Value::Int(1), Value::Int(2)]),
            )
            .unwrap(),
            Col::new(
                Arc::new(Field::new("e", ltype4.clone())),
                Arc::new(vec![
                    Value::List(Arc::new(
                        value::List::new(Float, &[Value::Float(1.0), Value::Float(2.0)]).unwrap(),
                    )),
                    Value::None,
                    Value::List(Arc::new(
                        value::List::new(Float, &[Value::Float(5.0), Value::Float(6.0)]).unwrap(),
                    )),
                ]),
            )
            .unwrap(),
            Col::new(
                Arc::new(Field::new("f", ltype5.clone())),
                Arc::new(vec![
                    Value::List(Arc::new(
                        value::List::new(
                            Type::optional(Int),
                            &[Value::Int(1), Value::None, Value::Int(2)],
                        )
                        .unwrap(),
                    )),
                    Value::None,
                    Value::List(Arc::new(
                        value::List::new(
                            Type::optional(Int),
                            &[Value::Int(3), Value::None, Value::Int(6)],
                        )
                        .unwrap(),
                    )),
                ]),
            )
            .unwrap(),
        ])
        .unwrap();
        df
    }

    fn default_df() -> Dataframe {
        Dataframe::new(vec![
            Col::from("a", Type::Int, vec![1, 2, 3]).unwrap(),
            Col::from("b", Type::Int, vec![11, 12, 13]).unwrap(),
            Col::from("c", Type::Float, vec![1.0, 2.0, 3.1]).unwrap(),
            Col::from("d", Type::String, vec!["1", "1.0", "Hi"]).unwrap(),
            Col::from("e", Type::Bool, vec![true, false, true]).unwrap(),
            Col::from("f", Type::Timestamp, vec![1, 2, 3]).unwrap(),
            Col::from(
                "g",
                Type::Optional(Box::new(Type::Int)),
                vec![Some(1), None, Some(3)],
            )
            .unwrap(),
            Col::from("h", Type::Float, vec![-1.0, 2.0, -3.1]).unwrap(),
            Col::from(
                "null_ints",
                Type::Optional(Box::new(Type::Int)),
                vec![None::<Value>, None, None],
            )
            .unwrap(),
            Col::from(
                "null_bools",
                Type::Optional(Box::new(Type::Bool)),
                vec![None::<Value>, None, None],
            )
            .unwrap(),
            Col::from(
                "null_floats",
                Type::Optional(Box::new(Type::Float)),
                vec![None::<Value>, None, None],
            )
            .unwrap(),
            Col::from(
                "null_strings",
                Type::Optional(Box::new(Type::String)),
                vec![Some("Hi"), None, Some("Bye")],
            ).unwrap(),
        ])
        .unwrap()
    }

    #[tokio::test]
    async fn test_unary_not() {
        use Type::*;
        let df = Dataframe::new(vec![
            Col::from("a", Int, vec![1, 2, 3]).unwrap(),
            Col::from("b", String, vec!["a", "b", "c"]).unwrap(),
            Col::from("c", Bool, vec![true, false, true]).unwrap(),
            Col::from("d", Float, vec![1.1, 2.2, 3.3]).unwrap(),
            Col::from(
                "e",
                Type::optional(Bool),
                vec![Some(true), None, Some(false)],
            )
            .unwrap(),
            Col::from("f", Type::optional(Int), vec![Some(1), None, Some(3)]).unwrap(),
        ])
        .unwrap();

        let cases = [
            // valid literals
            Case::new(not(lit(true))).matches(Bool, [false, false, false]),
            Case::new(not(lit(false))).matches(Bool, [true, true, true]),
            Case::new(not(lit(Value::None)))
                .matches(Type::optional(Bool), [None::<Value>, None, None]),
            // invalid literals
            Case::new(not(lit(1))).invalid(),
            Case::new(not(lit("hi"))).invalid(),
            Case::new(not(lit(1.0))).invalid(),
            // col refs
            Case::new(not(col("a"))).invalid(),
            Case::new(not(col("b"))).invalid(),
            Case::new(not(col("c"))).matches(Bool, [false, true, false]),
            Case::new(not(col("d"))).invalid(),
            Case::new(not(col("e")))
                .mismatches([Bool])
                .matches(Type::optional(Bool), [Some(false), None, Some(true)]),
            Case::new(not(col("f"))).invalid(),
            // composite - not of not
            Case::new(not(not(col("c")))).matches(Bool, [true, false, true]),
            Case::new(not(not(col("e"))))
                .matches(Type::optional(Bool), [Some(true), None, Some(false)]),
        ];
        check(df, cases);
    }

    #[test]
    fn test_lit() {
        use crate::types::{OneOf, Between};
        let df = Dataframe::new(vec![Col::from("a", Int, vec![1, 2, 3]).unwrap()]).unwrap();
        let cases = [
            Case::new(lit(1))
                .matches(Int, [1, 1, 1])
                .matches(Float, [1.0, 1.0, 1.0])
                .matches(Type::optional(Int), [Some(1), Some(1), Some(1)])
                .matches(Type::optional(Float), [Some(1.0), Some(1.0), Some(1.0)])
                .matches(
                    Between(Between::new(Int, 0.into(), 10.into(), false, false).unwrap()),
                    [1, 1, 1],
                )
                .matches(
                    OneOf(OneOf::new(Int, vec![1.into(), 2.into()]).unwrap()),
                    [1, 1, 1],
                )
                .mismatches([Bool, String, Type::List(Box::new(Int))]),
            Case::new(lit(1.0))
                .matches(Float, [1.0, 1.0, 1.0])
                .matches(Type::optional(Float), [Some(1.0), Some(1.0), Some(1.0)])
                .mismatches([
                    Int,
                    Bool,
                    String,
                    Type::optional(Int),
                    List(Box::new(Float)),
                ]),
            Case::new(lit(true))
                .matches(Bool, [true, true, true])
                .matches(Type::optional(Bool), [Some(true), Some(true), Some(true)])
                .mismatches([Int, Float, String, List(Box::new(Bool))]),
            Case::new(lit("hi"))
                .matches(String, ["hi", "hi", "hi"])
                .matches(Type::optional(String), [Some("hi"), Some("hi"), Some("hi")])
                .mismatches([Int, Float, Bool, List(Box::new(String))]),
            Case::new(lit(Value::None))
                .matches(Type::Null, [Value::None, Value::None, Value::None])
                .matches(Type::optional(Int), [None::<Value>, None, None])
                .matches(Type::optional(Float), [None::<Value>, None, None])
                .matches(Type::optional(Bool), [None::<Value>, None, None])
                .matches(Type::optional(String), [None::<Value>, None, None])
                .matches(Type::optional(Date), [None::<Value>, None, None])
                .matches(Type::optional(Timestamp), [None::<Value>, None, None])
                .mismatches([Int, Float, Bool, String, Date, Timestamp])
                .mismatches([Type::List(Box::new(Int))])
                .mismatches([Struct(Box::new(
                    types::StructType::new(
                        "somename".into(),
                        vec![Field::new("a".to_string(), Int)],
                    )
                    .unwrap(),
                ))])
                .mismatches([Decimal(types::DecimalType::new(5).unwrap())]),
        ];
        check(df, cases);
    }

    #[test]
    fn test_ref_matches() {
        use crate::value::List;
        let list = Col::from(
            "r",
            Type::List(Box::new(Type::Int)),
            [
                Value::List(Arc::new(
                    List::new(Type::Int, &[1.into(), 2.into(), 3.into()]).unwrap(),
                )),
                Value::List(Arc::new(
                    List::new(Type::Int, &[4.into(), 5.into()]).unwrap(),
                )),
                Value::List(Arc::new(List::new(Type::Int, &[6.into()]).unwrap())),
            ],
        )
        .unwrap();
        let df = Dataframe::new(vec![
            Col::from("a", Type::Int, vec![1, 2, 3]).unwrap(),
            Col::from("b", Type::String, vec!["a", "b", "c"]).unwrap(),
            Col::from("c", Type::Bool, vec![true, false, true]).unwrap(),
            Col::from("d", Type::Float, vec![1.1, 2.2, 3.3]).unwrap(),
            Col::from("e", Type::Timestamp, vec![1, 2, 3]).unwrap(),
            Col::from(
                "f",
                Type::List(Box::new(Type::Int)),
                list.values().iter().map(|v| v.clone()).collect_vec(),
            )
            .unwrap(),
        ])
        .unwrap();
        let cases = [
            Case::new(col("a"))
                .matches(Int, [1, 2, 3])
                .matches(Float, [1.0, 2.0, 3.0])
                .matches(Type::optional(Int), [Some(1), Some(2), Some(3)])
                .matches(Type::optional(Float), [Some(1.0), Some(2.0), Some(3.0)])
                .mismatches([
                    Bool,
                    String,
                    Timestamp,
                    Date,
                    List(Box::new(Int)),
                    Struct(Box::new(
                        types::StructType::new(
                            "somename".into(),
                            vec![Field::new("a".to_string(), Int)],
                        )
                        .unwrap(),
                    )),
                ]),
            Case::new(col("b"))
                .matches(String, ["a", "b", "c"])
                .matches(Type::optional(String), [Some("a"), Some("b"), Some("c")])
                .mismatches([
                    Int,
                    Float,
                    Bool,
                    Timestamp,
                    Date,
                    List(Box::new(String)),
                    Struct(Box::new(
                        types::StructType::new(
                            "somename".into(),
                            vec![Field::new("a".to_string(), String)],
                        )
                        .unwrap(),
                    )),
                ]),
            Case::new(col("c"))
                .matches(Bool, [true, false, true])
                .matches(Type::optional(Bool), [Some(true), Some(false), Some(true)])
                .mismatches([
                    Int,
                    Float,
                    String,
                    Timestamp,
                    Date,
                    List(Box::new(Bool)),
                    Struct(Box::new(
                        types::StructType::new(
                            "somename".into(),
                            vec![Field::new("a".to_string(), Bool)],
                        )
                        .unwrap(),
                    )),
                ]),
            Case::new(col("d"))
                .matches(Float, [1.1, 2.2, 3.3])
                .matches(Type::optional(Float), [Some(1.1), Some(2.2), Some(3.3)])
                .mismatches([
                    Int,
                    Bool,
                    String,
                    Timestamp,
                    Date,
                    Type::optional(Int),
                    List(Box::new(Float)),
                    Struct(Box::new(
                        types::StructType::new(
                            "somename".into(),
                            vec![Field::new("a".to_string(), Float)],
                        )
                        .unwrap(),
                    )),
                ]),
            Case::new(col("e"))
                .matches(Timestamp, [1, 2, 3])
                .matches(Type::optional(Timestamp), [Some(1), Some(2), Some(3)])
                .mismatches([
                    Int,
                    Bool,
                    String,
                    Float,
                    Date,
                    List(Box::new(Timestamp)),
                    Struct(Box::new(
                        types::StructType::new(
                            "somename".into(),
                            vec![Field::new("a".to_string(), Timestamp)],
                        )
                        .unwrap(),
                    )),
                ]),
            Case::new(col("f"))
                .matches(
                    List(Box::new(Int)),
                    list.values().iter().map(|v| v.clone()).collect_vec(),
                )
                .matches(
                    Type::optional(List(Box::new(Int))),
                    list.values().iter().map(|v| Some(v.clone())).collect_vec(),
                )
                .mismatches([
                    Int,
                    Bool,
                    String,
                    Float,
                    Date,
                    List(Box::new(Float)),
                    Struct(Box::new(
                        types::StructType::new(
                            "somename".into(),
                            vec![Field::new("a".to_string(), List(Box::new(Int)))],
                        )
                        .unwrap(),
                    )),
                ]),
        ];
        check(df, cases);
    }

    #[test]
    fn test_unary_neg() {
        let df = Dataframe::new(vec![
            Col::from("a", Int, vec![1, 2, 3]).unwrap(),
            Col::from("b", String, vec!["a", "b", "c"]).unwrap(),
            Col::from("c", Bool, vec![true, false, true]).unwrap(),
            Col::from("d", Float, vec![1.1, 2.2, 3.3]).unwrap(),
            Col::from("e", Timestamp, vec![1, 2, 3]).unwrap(),
            Col::from("f", Optional(Box::new(Int)), vec![Some(1), None, Some(3)]).unwrap(),
        ])
        .unwrap();
        let cases = [
            // some invalid cases
            Case::new(neg(lit(true))).invalid(),
            Case::new(neg(lit("hi"))).invalid(),
            Case::new(neg(col("b"))).invalid(),
            Case::new(neg(col("c"))).invalid(),
            Case::new(neg(col("e"))).invalid(),
            // negation of literals
            Case::new(neg(lit(1)))
                .matches(Int, [-1, -1, -1])
                .matches(Float, [-1.0, -1.0, -1.0])
                .matches(Type::optional(Int), [Some(-1), Some(-1), Some(-1)])
                .matches(Type::optional(Float), [Some(-1.0), Some(-1.0), Some(-1.0)])
                .mismatches([String, Bool, Timestamp, Date])
                .mismatches([List(Box::new(Int)), Map(Box::new(Int))]),
            Case::new(neg(lit(1.1)))
                .matches(Float, [-1.1, -1.1, -1.1])
                .matches(Type::optional(Float), [Some(-1.1), Some(-1.1), Some(-1.1)])
                .mismatches([Int, String, Bool, Timestamp, Type::optional(Int)])
                .mismatches([List(Box::new(Float)), Map(Box::new(Float))]),
            // negation of column refs
            Case::new(neg(col("a")))
                .matches(Int, [-1, -2, -3])
                .matches(Float, [-1.0, -2.0, -3.0])
                .matches(Type::optional(Int), [Some(-1), Some(-2), Some(-3)])
                .matches(Type::optional(Float), [Some(-1.0), Some(-2.0), Some(-3.0)])
                .mismatches([String, Bool, Timestamp])
                .mismatches([List(Box::new(Int)), Map(Box::new(Int))]),
            Case::new(neg(col("d")))
                .matches(Float, [-1.1, -2.2, -3.3])
                .matches(Type::optional(Float), [Some(-1.1), Some(-2.2), Some(-3.3)])
                .mismatches([Int, String, Bool, Timestamp, Type::optional(Int)])
                .mismatches([List(Box::new(Float)), Map(Box::new(Float))]),
            Case::new(neg(col("f")))
                .matches(Type::optional(Int), [Some(-1), None, Some(-3)])
                .matches(Type::optional(Float), [Some(-1.0), None, Some(-3.0)])
                .mismatches([Int, Float, String, Bool, Timestamp, List(Box::new(Int))])
                .mismatches([List(Box::new(Float)), Map(Box::new(Float))]),
        ];
        check(df, cases);
    }

    #[test]
    fn test_arithmetic_sub() {
        // same as test_arithmetic_add but with subtraction
        let df = Dataframe::new(vec![
            Col::from("a", Type::Int, vec![1, 2, 3]).unwrap(),
            Col::from("b", Type::Int, vec![11, 12, 13]).unwrap(),
            Col::from("c", Type::Float, vec![1.1, 2.1, 3.1]).unwrap(),
            Col::from("d", Type::String, vec!["hi", "bye", "something"]).unwrap(),
            Col::from("e", Type::Bool, vec![true, false, true]).unwrap(),
            Col::from("f", Type::Timestamp, vec![1, 2, 3]).unwrap(),
            Col::from(
                "g",
                Type::Optional(Box::new(Type::Int)),
                vec![Some(1), None, Some(3)],
            )
            .unwrap(),
        ])
        .unwrap();
        let cases = [
            // invalid subtraction using literals
            Case::new(lit("hi") - lit("bye")).invalid(),
            Case::new(lit(1) - lit("bye")).invalid(),
            Case::new(lit(true) - lit(1)).invalid(),
            Case::new(lit(1) - lit(true)).invalid(),
            Case::new(lit(true) - lit(false)).invalid(),
            // invalid subtraction using refs
            Case::new(col("a") - lit("bye")).invalid(),
            Case::new(col("a") - col("d")).invalid(),
            Case::new(col("a") - col("e")).invalid(),
            Case::new(col("a") - col("f")).invalid(),
            // subtraction of two integers or two floats
            Case::new(lit(1) - lit(2))
                .matches(Int, [-1, -1, -1])
                .matches(Float, [-1.0, -1.0, -1.0])
                .matches(Type::optional(Int), [Some(-1), Some(-1), Some(-1)])
                .matches(Type::optional(Float), [Some(-1.0), Some(-1.0), Some(-1.0)])
                .mismatches([String, Bool, Timestamp]),
            Case::new(lit(1.0) - lit(2.0))
                .matches(Float, [-1.0, -1.0, -1.0])
                .matches(Type::optional(Float), [Some(-1.0), Some(-1.0), Some(-1.0)])
                .mismatches([Int, String, Bool, Timestamp, Type::optional(Int)]),
            Case::new(col("a") - lit(2))
                .matches(Int, [-1, 0, 1])
                .matches(Float, [-1.0, 0.0, 1.0])
                .matches(Type::optional(Int), [Some(-1), Some(0), Some(1)])
                .matches(Type::optional(Float), [Some(-1.0), Some(0.0), Some(1.0)])
                .mismatches([String, Bool, Timestamp]),
            // here
            Case::new(col("a") - col("a"))
                .matches(Int, [0, 0, 0])
                .matches(Float, [0.0, 0.0, 0.0])
                .matches(Type::optional(Int), [Some(0), Some(0), Some(0)])
                .matches(Type::optional(Float), [Some(0.0), Some(0.0), Some(0.0)])
                .mismatches([String, Bool, Timestamp]),
            Case::new(col("a") - col("b"))
                .matches(Int, [-10, -10, -10])
                .matches(Float, [-10.0, -10.0, -10.0])
                .matches(Type::optional(Int), [Some(-10), Some(-10), Some(-10)])
                .matches(
                    Type::optional(Float),
                    [Some(-10.0), Some(-10.0), Some(-10.0)],
                )
                .mismatches([String, Bool, Timestamp]),
            Case::new(lit(1.5) - col("c"))
                .matches(Float, [0.4, -0.6, -1.6])
                .matches(Type::optional(Float), [Some(0.4), Some(-0.6), Some(-1.6)])
                .mismatches([Int, String, Bool, Timestamp]),
            // mix of int and float
            Case::new(lit(1) - lit(2.1))
                .matches(Float, [-1.1, -1.1, -1.1])
                .matches(Type::optional(Float), [Some(-1.1), Some(-1.1), Some(-1.1)])
                .mismatches([Int, String, Bool, Timestamp, Type::optional(Int)]),
            Case::new(col("a") - col("c"))
                .matches(Float, [-0.1, -0.1, -0.1])
                .matches(Type::optional(Float), [Some(-0.1), Some(-0.1), Some(-0.1)])
                .mismatches([Int, String, Bool, Timestamp, Type::optional(Int)]),
            // mix of int and float with optional
            Case::new(col("a") - col("g"))
                .matches(Optional(Box::new(Int)), [Some(0), None, Some(0)])
                .matches(Optional(Box::new(Float)), [Some(0.0), None, Some(0.0)])
                .mismatches([Float, String, Bool, Timestamp, Int]),
            Case::new(col("c") - col("g"))
                .matches(Optional(Box::new(Float)), [Some(0.1), None, Some(0.1)])
                .mismatches([Int, Float, String, Bool, Timestamp, Type::optional(Int)]),
            // some literal None
            Case::new(col("a") - lit(Value::None))
                .matches(Type::optional(Int), [None::<Value>, None, None])
                .matches(Type::optional(Float), [None::<Value>, None, None])
                .mismatches([Int, Float, Bool, String, Timestamp, Date]),
            Case::new(lit(Value::None) - lit(Value::None))
                .matches(Type::optional(Int), [None::<Value>, None, None])
                .matches(Type::optional(Float), [None::<Value>, None, None])
                .mismatches([
                    Int,
                    Float,
                    Bool,
                    String,
                    Timestamp,
                    Date,
                    Type::optional(Bool),
                    Type::optional(String),
                    Type::optional(Timestamp),
                    Type::optional(Date),
                ]),
        ];
        check(df, cases);
    }

    #[test]
    fn test_arithmetic_mul() {
        let df = Dataframe::new(vec![
            Col::from("a", Type::Int, vec![1, 2, 3]).unwrap(),
            Col::from("b", Type::Int, vec![11, 12, 13]).unwrap(),
            Col::from("c", Type::Float, vec![1.1, 2.1, 3.1]).unwrap(),
            Col::from("d", Type::String, vec!["hi", "bye", "something"]).unwrap(),
            Col::from("e", Type::Bool, vec![true, false, true]).unwrap(),
            Col::from("f", Type::Timestamp, vec![1, 2, 3]).unwrap(),
            Col::from(
                "g",
                Type::Optional(Box::new(Type::Int)),
                vec![Some(1), None, Some(3)],
            )
            .unwrap(),
        ])
        .unwrap();
        let cases = [
            // invalid multiplication using literals
            Case::new(lit("hi") * lit("bye")).invalid(),
            Case::new(lit(1) * lit("bye")).invalid(),
            Case::new(lit(true) * lit(1)).invalid(),
            Case::new(lit(1) * lit(true)).invalid(),
            Case::new(lit(true) * lit(false)).invalid(),
            // invalid multiplication using refs
            Case::new(col("a") * lit("bye")).invalid(),
            Case::new(col("a") * col("d")).invalid(),
            Case::new(col("a") * col("e")).invalid(),
            Case::new(col("a") * col("f")).invalid(),
            // multiplication of two integers or two floats
            Case::new(lit(1) * lit(2))
                .matches(Int, [2, 2, 2])
                .matches(Float, [2.0, 2.0, 2.0])
                .matches(Type::optional(Int), [Some(2), Some(2), Some(2)])
                .matches(Type::optional(Float), [Some(2.0), Some(2.0), Some(2.0)])
                .mismatches([String, Bool, Timestamp]),
            Case::new(lit(1.0) * lit(2.0))
                .matches(Float, [2.0, 2.0, 2.0])
                .matches(Type::optional(Float), [Some(2.0), Some(2.0), Some(2.0)])
                .mismatches([Int, String, Bool, Timestamp, Type::optional(Int)]),
            Case::new(col("a") * lit(2))
                .matches(Int, [2, 4, 6])
                .matches(Float, [2.0, 4.0, 6.0])
                .matches(Type::optional(Int), [Some(2), Some(4), Some(6)])
                .matches(Type::optional(Float), [Some(2.0), Some(4.0), Some(6.0)])
                .mismatches([String, Bool, Timestamp]),
            Case::new(col("a") * col("a"))
                .matches(Int, [1, 4, 9])
                .matches(Float, [1.0, 4.0, 9.0])
                .matches(Type::optional(Int), [Some(1), Some(4), Some(9)])
                .matches(Type::optional(Float), [Some(1.0), Some(4.0), Some(9.0)])
                .mismatches([String, Bool, Timestamp]),
            // mix of int and float
            Case::new(lit(1) * lit(2.1))
                .matches(Float, [2.1, 2.1, 2.1])
                .matches(Type::optional(Float), [Some(2.1), Some(2.1), Some(2.1)])
                .mismatches([Int, String, Bool, Timestamp, Type::optional(Int)]),
            // mix of int and float with optional
            Case::new(col("a") * col("g"))
                .matches(Optional(Box::new(Int)), [Some(1), None, Some(9)])
                .matches(Optional(Box::new(Float)), [Some(1.0), None, Some(9.0)])
                .mismatches([Float, String, Bool, Timestamp, Int]),
            Case::new(col("c") * col("g"))
                .matches(Optional(Box::new(Float)), [Some(1.1), None, Some(9.3)])
                .mismatches([Int, Float, String, Bool, Timestamp, Type::optional(Int)]),
            Case::new(col("a") * lit(Value::None))
                .matches(Type::optional(Int), [None::<Value>, None, None])
                .matches(Type::optional(Float), [None::<Value>, None, None])
                .mismatches([Int, Float, Bool, String, Timestamp, Date]),
            Case::new(lit(Value::None) * lit(Value::None))
                .matches(Type::optional(Int), [None::<Value>, None, None])
                .matches(Type::optional(Float), [None::<Value>, None, None])
                .mismatches([
                    Int,
                    Float,
                    Bool,
                    String,
                    Timestamp,
                    Date,
                    Type::optional(Bool),
                    Type::optional(String),
                ]),
        ];
        check(df, cases);
    }

    // TODO: write tests for division, modulo
    // TODO: write tests for comparison operators
    // TODO: write tests for complex expressions
    // TODO: write tests for dict and string functions
    // TODO: some literals for lists etc?
    #[test]
    fn test_arithmetic_add() {
        let df = Dataframe::new(vec![
            Col::from("a", Type::Int, vec![1, 2, 3]).unwrap(),
            Col::from("b", Type::Int, vec![11, 12, 13]).unwrap(),
            Col::from("c", Type::Float, vec![1.1, 2.1, 3.1]).unwrap(),
            Col::from("d", Type::String, vec!["hi", "bye", "something"]).unwrap(),
            Col::from("e", Type::Bool, vec![true, false, true]).unwrap(),
            Col::from("f", Type::Timestamp, vec![1, 2, 3]).unwrap(),
            Col::from(
                "g",
                Type::Optional(Box::new(Type::Int)),
                vec![Some(1), None, Some(3)],
            )
            .unwrap(),
        ])
        .unwrap();
        let cases = [
            // invalid addition using literals
            Case::new(lit("hi") + lit("bye")).invalid(),
            Case::new(lit(1) + lit("bye")).invalid(),
            Case::new(lit(true) + lit(1)).invalid(),
            Case::new(lit(1) + lit(true)).invalid(),
            Case::new(lit(true) + lit(false)).invalid(),
            // invalid addition using refs
            Case::new(col("a") + lit("bye")).invalid(),
            Case::new(col("a") + col("d")).invalid(),
            Case::new(col("a") + col("e")).invalid(),
            Case::new(col("a") + col("f")).invalid(),
            // addition of two integers or two floats
            Case::new(lit(1) + lit(2))
                .matches(Int, [3, 3, 3])
                .matches(Float, [3.0, 3.0, 3.0])
                .matches(Type::optional(Int), [Some(3), Some(3), Some(3)])
                .matches(Type::optional(Float), [Some(3.0), Some(3.0), Some(3.0)])
                .mismatches([String, Bool, Timestamp, Date])
                .mismatches([Struct(Box::new(
                    types::StructType::new(
                        "somename".into(),
                        vec![Field::new("a".to_string(), Int)],
                    )
                    .unwrap(),
                ))])
                .mismatches([Decimal(types::DecimalType::new(5).unwrap())]),
            Case::new(lit(1.0) + lit(2.0))
                .matches(Float, [3.0, 3.0, 3.0])
                .matches(Type::optional(Float), [Some(3.0), Some(3.0), Some(3.0)])
                .mismatches([Int, String, Bool, Timestamp, Type::optional(Int)]),
            Case::new(col("a") + lit(2))
                .matches(Int, [3, 4, 5])
                .matches(Float, [3.0, 4.0, 5.0])
                .matches(Type::optional(Int), [Some(3), Some(4), Some(5)])
                .matches(Type::optional(Float), [Some(3.0), Some(4.0), Some(5.0)])
                .mismatches([String, Bool, Timestamp, Date]),
            Case::new(col("a") + col("a"))
                .matches(Int, [2, 4, 6])
                .matches(Float, [2.0, 4.0, 6.0])
                .matches(Type::optional(Int), [Some(2), Some(4), Some(6)])
                .matches(Type::optional(Float), [Some(2.0), Some(4.0), Some(6.0)])
                .mismatches([String, Bool, Timestamp, Date]),
            Case::new(col("a") + col("b"))
                .matches(Int, [12, 14, 16])
                .matches(Type::optional(Int), [Some(12), Some(14), Some(16)])
                .matches(Float, [12.0, 14.0, 16.0])
                .matches(Type::optional(Float), [Some(12.0), Some(14.0), Some(16.0)])
                .mismatches([String, Bool, Timestamp]),
            Case::new(lit(1.5) + col("c"))
                .matches(Float, [2.6, 3.6, 4.6])
                .matches(Type::optional(Float), [Some(2.6), Some(3.6), Some(4.6)])
                .mismatches([Int, String, Bool, Timestamp, Type::optional(Int)]),
            // mix of int and float
            Case::new(lit(1) + lit(2.1))
                .matches(Float, [3.1, 3.1, 3.1])
                .matches(Type::optional(Float), [Some(3.1), Some(3.1), Some(3.1)])
                .mismatches([Int, String, Bool, Timestamp, Type::optional(Int)]),
            Case::new(col("a") + col("c"))
                .matches(Float, [2.1, 4.1, 6.1])
                .matches(Type::optional(Float), [Some(2.1), Some(4.1), Some(6.1)])
                .mismatches([Int, String, Bool, Timestamp, Type::optional(Int)]),
            // mix of int and float with optional
            Case::new(col("a") + col("g"))
                .matches(Optional(Box::new(Int)), [Some(2), None, Some(6)])
                .matches(Optional(Box::new(Float)), [Some(2.0), None, Some(6.0)])
                .mismatches([Float, String, Bool, Timestamp, Int]),
            Case::new(col("c") + col("g"))
                .matches(Optional(Box::new(Float)), [Some(2.1), None, Some(6.1)])
                .mismatches([Int, String, Bool, Timestamp, Type::optional(Int), Float]),
            // cases involving none literal
            Case::new(col("a") + lit(Value::None))
                .matches(Type::optional(Int), [None::<Value>, None, None])
                .matches(Type::optional(Float), [None::<Value>, None, None])
                .mismatches([Int, Float, Bool, String, Timestamp, Date]),
            Case::new(lit(Value::None) + lit(Value::None))
                .matches(Type::optional(Int), [None::<Value>, None, None])
                .matches(Type::optional(Float), [None::<Value>, None, None])
                .mismatches([
                    Int,
                    Float,
                    Bool,
                    String,
                    Timestamp,
                    Date,
                    Type::optional(Bool),
                    Type::optional(String),
                ]),
        ];
        check(df, cases);
    }

    #[test]
    fn test_logical_and_or() {
        let df = Dataframe::new(vec![
            Col::from("a", Type::Int, vec![1, 2, 3]).unwrap(),
            Col::from("c", Type::Float, vec![1.1, 2.1, 3.1]).unwrap(),
            Col::from("d", Type::String, vec!["hi", "bye", "something"]).unwrap(),
            Col::from("e", Type::Bool, vec![true, false, true]).unwrap(),
            Col::from("f", Type::Timestamp, vec![1, 2, 3]).unwrap(),
            Col::from(
                "g",
                Type::Optional(Box::new(Type::Bool)),
                vec![Some(true), None, Some(false)],
            )
            .unwrap(),
        ])
        .unwrap();
        let and_cases = [
            //invalids ands
            Case::new(col("a").and(col("c"))).invalid(),
            Case::new(col("a").and(col("d"))).invalid(),
            Case::new(col("a").and(col("e"))).invalid(),
            Case::new(col("a").and(col("f"))).invalid(),
            Case::new(col("a").and(col("g"))).invalid(),
            // valid ands
            Case::new(col("e").and(lit(true)))
                .matches(Bool, [true, false, true])
                .matches(Type::optional(Bool), [Some(true), Some(false), Some(true)])
                .mismatches([Int, Float, String, Timestamp]),
            Case::new(col("e").and(lit(false)))
                .matches(Bool, [false, false, false])
                .matches(
                    Type::optional(Bool),
                    [Some(false), Some(false), Some(false)],
                )
                .mismatches([Int, Float, String, Timestamp]),
            Case::new(col("e").and(lit(true)))
                .matches(Bool, [true, false, true])
                .matches(Type::optional(Bool), [Some(true), Some(false), Some(true)])
                .mismatches([Int, Float, String, Timestamp]),
            // involving optional
            Case::new(lit(Value::None).and(lit(Value::None)))
                .matches(Optional(Box::new(Bool)), [None::<Value>, None, None])
                .mismatches([Int, Float, String, Timestamp, Bool]),
            Case::new(col("e").and(lit(Value::None)))
                .matches(Optional(Box::new(Bool)), [None, Some(false), None])
                .mismatches([Int, Float, String, Timestamp, Bool]),
            Case::new(col("e").and(col("g")))
                .matches(
                    Optional(Box::new(Bool)),
                    [Some(true), Some(false), Some(false)],
                )
                .mismatches([Int, Float, String, Timestamp, Bool]),
            Case::new(not(col("e")).and(col("g")))
                .matches(Optional(Box::new(Bool)), [Some(false), None, Some(false)])
                .mismatches([Int, Float, String, Timestamp, Bool]),
        ];
        let or_cases = [
            //invalids ors
            Case::new(col("a").or(col("c"))).invalid(),
            Case::new(col("a").or(col("d"))).invalid(),
            Case::new(col("a").or(col("e"))).invalid(),
            Case::new(col("a").or(col("f"))).invalid(),
            Case::new(col("a").or(col("g"))).invalid(),
            // valid ors
            Case::new(col("e").or(lit(true)))
                .matches(Bool, [true, true, true])
                .matches(Type::optional(Bool), [Some(true), Some(true), Some(true)])
                .mismatches([Int, Float, String, Timestamp]),
            Case::new(col("e").or(lit(false)))
                .matches(Bool, [true, false, true])
                .matches(Type::optional(Bool), [Some(true), Some(false), Some(true)])
                .mismatches([Int, Float, String, Timestamp]),
            Case::new(col("e").or(col("e")))
                .matches(Bool, [true, false, true])
                .matches(Type::optional(Bool), [Some(true), Some(false), Some(true)])
                .mismatches([Int, Float, String, Timestamp]),
            // involving optional
            Case::new(lit(Value::None).or(lit(Value::None)))
                .matches(Optional(Box::new(Bool)), [None::<Value>, None, None])
                .mismatches([Int, Float, String, Timestamp, Bool]),
            Case::new(col("e").or(lit(Value::None)))
                .matches(Optional(Box::new(Bool)), [Some(true), None, Some(true)])
                .mismatches([Int, Float, String, Timestamp, Bool]),
            Case::new(col("e").or(col("g")))
                .matches(Optional(Box::new(Bool)), [Some(true), None, Some(true)])
                .mismatches([Int, Float, String, Timestamp, Bool]),
            Case::new(not(col("e")).or(col("g")))
                .matches(
                    Optional(Box::new(Bool)),
                    [Some(true), Some(true), Some(false)],
                )
                .mismatches([Int, Float, String, Timestamp, Bool]),
        ];
        let cases = and_cases
            .iter()
            .chain(or_cases.iter())
            .cloned()
            .collect_vec();
        check(df, cases);
    }

    #[test]
    fn test_complex_expr() {
        let df = Dataframe::new(vec![
            Col::from("a", Type::Int, vec![1, 2, 3]).unwrap(),
            Col::from("b", Type::Int, vec![11, 12, 13]).unwrap(),
            Col::from("c", Type::Float, vec![1.1, 2.1, 3.1]).unwrap(),
            Col::from("d", Type::String, vec!["hi", "bye", "something"]).unwrap(),
            Col::from("e", Type::Bool, vec![true, false, true]).unwrap(),
            Col::from("f", Type::Timestamp, vec![1, 2, 3]).unwrap(),
            Col::from(
                "g",
                Type::Optional(Box::new(Type::Int)),
                vec![Some(1), None, Some(3)],
            )
            .unwrap(),
        ])
        .unwrap();
        let cases = [
            Case::new(col("a").and(col("b")).or(col("c"))).invalid(),
            Case::new(col("a").neq(col("g")).and(lit(Value::None)))
                .matches(Optional(Box::new(Bool)), [Some(false), None, Some(false)])
                .mismatches([Int, Float, String, Timestamp, Bool]),
            Case::new(col("a").add(lit(10)).eq(col("b")))
                .matches(Bool, [true, true, true])
                .matches(Type::optional(Bool), [Some(true), Some(true), Some(true)])
                .mismatches([Int, Float, String, Timestamp]),
            Case::new(col("b").sub(col("c").add(col("g"))))
                .matches(Type::optional(Float), [Some(8.9), None, Some(6.9)])
                .mismatches([Int, Bool, Timestamp, Float, Type::optional(Int)]),
            Case::new(col("a").gt(col("b").sub(col("a"))))
                .matches(Bool, [false, false, false])
                .matches(
                    Type::optional(Bool),
                    [Some(false), Some(false), Some(false)],
                )
                .mismatches([Float, String, Timestamp]),
            Case::new(col("a") + col("b") - col("g"))
                .matches(
                    Type::optional(Int),
                    [Some(1 + 11 - 1), None, Some(3 + 13 - 3)],
                )
                .matches(
                    Type::optional(Float),
                    [Some(1.0 + 11.0 - 1.0), None, Some(3.0 + 13.0 - 3.0)],
                )
                .mismatches([Float, String, Bool, Timestamp, Int]),
            Case::new(lit(Value::None).gte(lit(Value::None)))
                .matches(Optional(Box::new(Bool)), [None::<Value>, None, None])
                .mismatches([Int, Float, String, Timestamp, Bool]),
            Case::new(lit(Value::None).gte(lit(Value::None) + lit(Value::None)))
                .matches(Optional(Box::new(Bool)), [None::<Value>, None, None])
                .mismatches([Int, Float, String, Timestamp, Bool]),
        ];
        check(df, cases);
    }

    #[test]
    fn test_eq_neq() {
        let df = Dataframe::new(vec![
            Col::from("a", Type::Int, vec![1, 2, 3]).unwrap(),
            Col::from("b", Type::Int, vec![11, 12, 13]).unwrap(),
            Col::from("c", Type::Float, vec![1.0, 2.0, 3.1]).unwrap(),
            Col::from("d", Type::String, vec!["1", "1.0", "hi"]).unwrap(),
            Col::from("e", Type::Bool, vec![true, false, true]).unwrap(),
            Col::from("f", Type::Timestamp, vec![1, 2, 3]).unwrap(),
            Col::from(
                "g",
                Type::Optional(Box::new(Type::Int)),
                vec![Some(1), None, Some(3)],
            )
            .unwrap(),
        ])
        .unwrap();
        let b = binary;
        use BinOp::*;
        // we will now rewrite/improve cases below to use Case2
        let eq_cases = [
            // invalid equality
            Case::new(b(lit(1), Eq, lit("1"))).invalid(),
            Case::new(b(col("a"), Eq, col("d"))).invalid(),
            Case::new(b(col("a"), Eq, col("e"))).invalid(),
            Case::new(b(col("d"), Eq, col("e"))).invalid(),
            // basic equality in same type
            Case::new(b(lit(1), Eq, lit(Value::None)))
            .produces(Type::optional(Bool), [None::<Value>, None, None]),
            Case::new(b(lit(Value::None), Eq, lit(Value::None)))
                .produces(Type::optional(Bool), [None::<Value>, None, None]),
            Case::new(b(lit(1), Eq, lit(1)))
                .matches(Bool, [true, true, true])
                .matches(Type::optional(Bool), [Some(true), Some(true), Some(true)])
                .mismatches([Int, Float, String, Timestamp, Type::optional(Int)]),
            Case::new(b(lit(1), Eq, lit(2)))
                .matches(Bool, [false, false, false])
                .matches(
                    Type::optional(Bool),
                    [Some(false), Some(false), Some(false)],
                )
                .mismatches([Int, Float, String, Timestamp, Type::optional(Int)]),
            Case::new(b(col("a"), Eq, lit(1)))
                .matches(Bool, [true, false, false])
                .matches(Type::optional(Bool), [Some(true), Some(false), Some(false)])
                .mismatches([Int, Float, String, Timestamp, Type::optional(Int)]),
            Case::new(b(lit(3.1), Eq, col("c")))
                .matches(Bool, [false, false, true])
                .matches(Type::optional(Bool), [Some(false), Some(false), Some(true)])
                .mismatches([Int, Float, String, Timestamp, Type::optional(Int)]),
            Case::new(b(lit("1"), Eq, col("d")))
                .matches(Bool, [true, false, false])
                .matches(Type::optional(Bool), [Some(true), Some(false), Some(false)])
                .mismatches([Int, Float, String, Timestamp, Type::optional(Int)]),
            Case::new(b(lit(false), Eq, col("e")))
                .matches(Bool, [false, true, false])
                .matches(Type::optional(Bool), [Some(false), Some(true), Some(false)])
                .mismatches([Int, Float, String, Timestamp, Type::optional(Int)]),
            Case::new(b(col("a"), Eq, col("a")))
                .matches(Bool, [true, true, true])
                .matches(Type::optional(Bool), [Some(true), Some(true), Some(true)])
                .mismatches([Int, Float, String, Timestamp, Type::optional(Int)]),
            Case::new(b(col("a"), Eq, col("b")))
                .matches(Bool, [false, false, false])
                .matches(
                    Type::optional(Bool),
                    [Some(false), Some(false), Some(false)],
                )
                .mismatches([Int, Float, String, Timestamp, Type::optional(Int)]),
            // int / float equality
            Case::new(b(lit(1), Eq, lit(1.0)))
                .matches(Bool, [true, true, true])
                .matches(Type::optional(Bool), [Some(true), Some(true), Some(true)])
                .mismatches([Int, Float, String, Timestamp, Type::optional(Float)]),
            Case::new(b(col("a"), Eq, col("c")))
                .matches(Bool, [true, true, false])
                .matches(Type::optional(Bool), [Some(true), Some(true), Some(false)])
                .mismatches([Int, Float, String, Timestamp, Type::optional(Float)]),
            // optional cases
            Case::new(b(col("a"), Eq, col("g")))
                .matches(Optional(Box::new(Bool)), [Some(true), None, Some(true)])
                .matches(Optional(Box::new(Bool)), [Some(true), None, Some(true)])
                .mismatches([Int, Float, String, Timestamp, Bool, Type::optional(Int)]),
            Case::new(b(col("c"), Eq, col("g")))
                .matches(Optional(Box::new(Bool)), [Some(true), None, Some(false)])
                .mismatches([Int, Float, String, Timestamp, Bool])
                .mismatches([Type::optional(Int)]),
        ];

        let mut cases = vec![];
        for case in eq_cases {
            cases.push(case.clone());
            // now convert to neq case
            // expr changes from Eq op to Neq op and matches change from true to false
            let mut new = case.clone();
            new.expr = match new.expr {
                Expr::Binary { left, right, .. } => Expr::Binary {
                    op: Neq,
                    left,
                    right,
                },
                _ => unreachable!("expected binary expr"),
            };
            for (_, values) in new.matches.iter_mut() {
                for v in values.iter_mut() {
                    match v {
                        Value::Bool(b) => *b = !*b,
                        _ => {}
                    }
                }
            }
            cases.push(new);
        }
        check(df, cases);
    }

    #[test]
    fn test_isnull() {
        let df = default_df();
        let cases = [
            // never invalid, even if the column is not nullable
            Case::new(isnull(lit(1)))
                .matches(Bool, [false, false, false])
                .matches(
                    Type::optional(Bool),
                    [Some(false), Some(false), Some(false)],
                )
                .mismatches([Int, Float, String, Timestamp]),
            Case::new(isnull(col("a")))
                .matches(Bool, [false, false, false])
                .matches(
                    Type::optional(Bool),
                    [Some(false), Some(false), Some(false)],
                )
                .mismatches([Int, Float, String, Timestamp]),
            Case::new(isnull(col("g")))
                .matches(Bool, [false, true, false])
                .matches(Type::optional(Bool), [Some(false), Some(true), Some(false)])
                .mismatches([Int, Float, String, Timestamp]),
            Case::new(isnull(lit(Value::None)))
                .matches(Bool, [true, true, true])
                .matches(Type::optional(Bool), [Some(true), Some(true), Some(true)])
                .mismatches([Int, Float, String, Timestamp]),
        ];
        check(df, cases);
    }

    #[test]
    fn test_fillnull() {
        let df = default_df();
        let cases = [
            // invalid when expr/default aren't compatible
            Case::new(fillnull(lit(1), lit("1"))).invalid(),
            Case::new(fillnull(col("a"), lit("1"))).invalid(),
            Case::new(fillnull(lit(1), col("d"))).invalid(),
            // valid cases
            Case::new(fillnull(lit(1), lit(2)))
                .matches(Int, [1, 1, 1])
                .matches(Type::optional(Int), [Some(1), Some(1), Some(1)])
                .matches(Float, [1.0, 1.0, 1.0])
                .matches(Type::optional(Float), [Some(1.0), Some(1.0), Some(1.0)])
                .mismatches([String, Bool, Timestamp]),
            Case::new(fillnull(col("a"), lit(2)))
                .matches(Int, [1, 2, 3])
                .matches(Type::optional(Int), [Some(1), Some(2), Some(3)])
                .matches(Float, [1.0, 2.0, 3.0])
                .matches(Type::optional(Float), [Some(1.0), Some(2.0), Some(3.0)])
                .mismatches([String, Bool, Timestamp]),
            Case::new(fillnull(col("g"), col("a")))
                .matches(Type::optional(Int), [Some(1), Some(2), Some(3)])
                .matches(Type::optional(Float), [Some(1.0), Some(2.0), Some(3.0)])
                .mismatches([String, Bool, Timestamp]),
            Case::new(fillnull(col("g"), lit(3.3)))
                .matches(Float, [1.0, 3.3, 3.0])
                .matches(Type::optional(Float), [Some(1.0), Some(3.3), Some(3.0)])
                .mismatches([Int, String, Bool, Timestamp]),
            Case::new(fillnull(lit(Value::None), lit(1)))
                .matches(Int, [1, 1, 1])
                .matches(Type::optional(Int), [Some(1), Some(1), Some(1)])
                .matches(Float, [1.0, 1.0, 1.0])
                .matches(Type::optional(Float), [Some(1.0), Some(1.0), Some(1.0)])
                .mismatches([String, Bool, Timestamp]),
            Case::new(fillnull(col("g"), lit(Value::None)))
                .matches(Optional(Box::new(Int)), [Some(1), None, Some(3)])
                .matches(Optional(Box::new(Float)), [Some(1.0), None, Some(3.0)])
                .mismatches([Float, Bool, Timestamp, Int, Type::optional(Bool)]),
            Case::new(fillnull(lit(Value::None), lit(Value::None)))
                .matches(Optional(Box::new(Int)), [None::<Value>, None, None])
                .matches(Optional(Box::new(Float)), [None::<Value>, None, None])
                .matches(Optional(Box::new(Bool)), [None::<Value>, None, None])
                .mismatches([String, Bool, Timestamp, Int]),
        ];
        check(df, cases);
    }

    #[test]
    fn test_when() {
        let df = default_df();
        let cases = [
            // some invalid cases
            // when doesn't evaluate to bool
            Case::new(when(lit(1), lit("one"))).invalid(),
            Case::new(when(col("a"), lit("one"))).invalid(),
            // two whens, oen of them invalid
            Case::new(when(col("a").eq(lit(1)), lit("one")).when(lit(1), lit("one"))).invalid(),
            // then/otherwise can not be promoted to the same type
            Case::new(when(col("a").eq(lit(1)), lit("one")).otherwise(lit(1))).invalid(),
            // valid cases
            Case::new(when(col("a").eq(lit(1)), lit("one")).otherwise(lit("not one")))
                .matches(String, ["one", "not one", "not one"])
                .matches(
                    Type::optional(String),
                    [Some("one"), Some("not one"), Some("not one")],
                )
                .mismatches([Int, Float, Bool, Timestamp]),
            Case::new(when(lit(true), col("d")).otherwise(lit("not one")))
                .matches(String, ["1", "1.0", "Hi"])
                .mismatches([Int, Float, Bool, Timestamp]),
            Case::new(when(lit(Value::None), lit(1)).otherwise(lit(2.0)))
                .matches(Float, [2.0, 2.0, 2.0])
                .matches(Type::optional(Float), [Some(2.0), Some(2.0), Some(2.0)])
                .mismatches([Int, String, Bool, Timestamp]),
            // without otherwise
            Case::new(when(col("a").eq(lit(1)), lit("one")))
                .matches(Type::optional(String), [Some("one"), None, None])
                .mismatches([String, Int, Float, Bool, Timestamp]),
            // multiple when
            Case::new(
                when(col("a").eq(lit(1)), lit("one"))
                    .when(col("a").eq(lit(2)), lit("two"))
                    .otherwise(lit("not one or two")),
            )
            .matches(String, ["one", "two", "not one or two"])
            .matches(
                Type::optional(String),
                [Some("one"), Some("two"), Some("not one or two")],
            )
            .mismatches([Int, Float, Bool, Timestamp]),
            // two thens, both with nones
            Case::new(
                when(col("a").eq(lit(1)), lit(Value::None))
                    .when(col("a").eq(lit(2)), lit(Value::None)),
            )
            .matches(Type::optional(Int), [None::<Value>, None, None]),
            // two thens, one int, one float without otherwise
            Case::new(when(col("a").eq(lit(1)), lit(1)).when(col("a").eq(lit(2)), lit(2.0)))
                .matches(Type::optional(Float), [Some(1.0), Some(2.0), None])
                .mismatches([Int, String, Bool, Float]),
            // three whens + otherwise, each having condition on different column
            Case::new(
                when(col("a").eq(lit(1)), lit("one"))
                    .when(col("b").eq(lit(12)), lit("twelve"))
                    .when(col("c").eq(lit(3.1)), lit("three point one"))
                    .otherwise(lit(Value::None)),
            )
            .matches(
                Type::optional(String),
                [Some("one"), Some("twelve"), Some("three point one")],
            )
            .mismatches([Int, Float, Bool, String]),
        ];
        check(df, cases);
    }

    #[test]
    fn test_lca() {
        let cases = [
            (Int, Int, Some(Int)),
            (Int, Float, Some(Float)),
            (Int, String, None),
            (Int, Type::optional(Int), Some(Type::optional(Int))),
            (Int, Type::optional(Float), Some(Type::optional(Float))),
            (Type::optional(Int), Float, Some(Type::optional(Float))),
            (Int, Type::Optional(Box::new(String)), None),
            (Int, Bool, None),
            (Null, Int, Some(Type::optional(Int))),
            (Null, Float, Some(Type::optional(Float))),
            (Null, Type::optional(Int), Some(Type::optional(Int))),
            (Null, Type::optional(Float), Some(Type::optional(Float))),
            (Null, String, Some(Type::optional(String))),
            (Null, Type::optional(String), Some(Type::optional(String))),
            (Null, Bool, Some(Type::optional(Bool))),
            (Null, Type::optional(Bool), Some(Type::optional(Bool))),
            (Null, Null, Some(Null)),
        ];
        for (t1, t2, expected) in cases {
            let t1 = Type::from(t1);
            let t2 = Type::from(t2);
            let expected = expected.map(Type::from);
            assert_eq!(lca(&t1, &t2), expected, "lca({}, {}) failed", t1, t2);
            assert_eq!(lca(&t2, &t1), expected, "lca({}, {}) failed", t2, t1);
        }
    }

    #[test]
    fn test_floor_ceil() {
        let df = default_df();
        let cases = [
            Case::new(floor(col("a")))
                .matches(Int, [1, 2, 3])
                .matches(Float, [1.0, 2.0, 3.0])
                .matches(Type::optional(Int), [Some(1), Some(2), Some(3)])
                .matches(Type::optional(Float), [Some(1.0), Some(2.0), Some(3.0)])
                .mismatches([String, Bool, Timestamp]),
            Case::new(ceil(col("a")))
                .matches(Int, [1, 2, 3])
                .matches(Float, [1.0, 2.0, 3.0])
                .matches(Type::optional(Int), [Some(1), Some(2), Some(3)])
                .matches(Type::optional(Float), [Some(1.0), Some(2.0), Some(3.0)])
                .mismatches([String, Bool, Timestamp]),
            Case::new(floor(lit(1.1)))
                .matches(Int, [1, 1, 1])
                .matches(Float, [1.0, 1.0, 1.0])
                .matches(Type::optional(Int), [Some(1), Some(1), Some(1)])
                .matches(Type::optional(Float), [Some(1.0), Some(1.0), Some(1.0)])
                .mismatches([String, Bool, Timestamp]),
            Case::new(ceil(lit(1.1)))
                .matches(Int, [2, 2, 2])
                .matches(Float, [2.0, 2.0, 2.0])
                .matches(Type::optional(Int), [Some(2), Some(2), Some(2)])
                .matches(Type::optional(Float), [Some(2.0), Some(2.0), Some(2.0)])
                .mismatches([String, Bool, Timestamp]),
            Case::new(floor(lit(2)))
                .matches(Int, [2, 2, 2])
                .matches(Float, [2.0, 2.0, 2.0])
                .matches(Type::optional(Int), [Some(2), Some(2), Some(2)])
                .matches(Type::optional(Float), [Some(2.0), Some(2.0), Some(2.0)])
                .mismatches([String, Bool, Timestamp]),
            Case::new(ceil(lit(2)))
                .matches(Int, [2, 2, 2])
                .matches(Float, [2.0, 2.0, 2.0])
                .matches(Type::optional(Int), [Some(2), Some(2), Some(2)])
                .matches(Type::optional(Float), [Some(2.0), Some(2.0), Some(2.0)])
                .mismatches([String, Bool, Timestamp]),
            Case::new(floor(lit(Value::None)))
                .matches(Type::optional(Int), [None::<Value>, None, None])
                .matches(Type::optional(Float), [None::<Value>, None, None])
                .mismatches([Int, Float, String, Bool, Timestamp]),
            Case::new(ceil(lit(Value::None)))
                .matches(Type::optional(Int), [None::<Value>, None, None])
                .matches(Type::optional(Float), [None::<Value>, None, None])
                .mismatches([Int, Float, String, Bool, Timestamp]),
            Case::new(floor(lit(1.3) + lit(1.1) + lit(Value::None)))
                .matches(Type::optional(Int), [None::<Value>, None, None])
                .matches(Type::optional(Float), [None::<Value>, None, None])
                .mismatches([Int, Float, String, Bool, Timestamp]),
            Case::new(ceil(lit(1.3) + lit(1.1) + lit(Value::None)))
                .matches(Type::optional(Int), [None::<Value>, None, None])
                .matches(Type::optional(Float), [None::<Value>, None, None])
                .mismatches([Int, Float, String, Bool, Timestamp]),
            Case::new(floor(lit(2.1) - lit(5)))
                .matches(Int, [-3, -3, -3])
                .matches(Float, [-3.0, -3.0, -3.0])
                .matches(Type::optional(Int), [Some(-3), Some(-3), Some(-3)])
                .matches(Type::optional(Float), [Some(-3.0), Some(-3.0), Some(-3.0)])
                .mismatches([String, Bool, Timestamp]),
            Case::new(ceil(lit(2.1) - lit(5)))
                .matches(Int, [-2, -2, -2])
                .matches(Float, [-2.0, -2.0, -2.0])
                .matches(Type::optional(Int), [Some(-2), Some(-2), Some(-2)])
                .matches(Type::optional(Float), [Some(-2.0), Some(-2.0), Some(-2.0)])
                .mismatches([String, Bool, Timestamp]),
            // some columns
            Case::new(floor(col("c")))
                .matches(Int, [1, 2, 3])
                .matches(Float, [1.0, 2.0, 3.0])
                .matches(Type::optional(Int), [Some(1), Some(2), Some(3)])
                .matches(Type::optional(Float), [Some(1.0), Some(2.0), Some(3.0)])
                .mismatches([String, Bool, Timestamp]),
            Case::new(ceil(col("c")))
                .matches(Int, [1, 2, 4])
                .matches(Float, [1.0, 2.0, 4.0])
                .matches(Type::optional(Int), [Some(1), Some(2), Some(4)])
                .matches(Type::optional(Float), [Some(1.0), Some(2.0), Some(4.0)])
                .mismatches([String, Bool, Timestamp]),
            Case::new(floor(col("c") + col("a")))
                .matches(Int, [2, 4, 6])
                .matches(Float, [2.0, 4.0, 6.0])
                .matches(Type::optional(Int), [Some(2), Some(4), Some(6)])
                .matches(Type::optional(Float), [Some(2.0), Some(4.0), Some(6.0)])
                .mismatches([String, Bool, Timestamp]),
            Case::new(ceil(col("c") + col("a")))
                .matches(Int, [2, 4, 7])
                .matches(Float, [2.0, 4.0, 7.0])
                .matches(Type::optional(Int), [Some(2), Some(4), Some(7)])
                .matches(Type::optional(Float), [Some(2.0), Some(4.0), Some(7.0)])
                .mismatches([String, Bool, Timestamp]),
            Case::new(floor(col("c") + col("g")))
                .matches(Optional(Box::new(Int)), [Some(2), None, Some(6)])
                .matches(Optional(Box::new(Float)), [Some(2.0), None, Some(6.0)])
                .mismatches([String, Bool, Timestamp, Int, Float]),
            Case::new(ceil(col("c") + col("g")))
                .matches(Optional(Box::new(Int)), [Some(2), None, Some(7)])
                .matches(Optional(Box::new(Float)), [Some(2.0), None, Some(7.0)])
                .mismatches([String, Bool, Timestamp, Int, Float]),
        ];
        check(df, cases);
    }

    #[test]
    fn test_round() {
        let df = default_df();
        let cases = [
            Case::new(round(lit(1.1)))
                .matches(Int, [1, 1, 1])
                .matches(Float, [1.0, 1.0, 1.0])
                .matches(Type::optional(Int), [Some(1), Some(1), Some(1)])
                .matches(Type::optional(Float), [Some(1.0), Some(1.0), Some(1.0)])
                .mismatches([String, Bool, Timestamp]),
            Case::new(roundto(lit(1.1), 0))
                .matches(Int, [1, 1, 1])
                .matches(Float, [1.0, 1.0, 1.0])
                .matches(Type::optional(Int), [Some(1), Some(1), Some(1)])
                .matches(Type::optional(Float), [Some(1.0), Some(1.0), Some(1.0)])
                .mismatches([String, Bool, Timestamp]),
            Case::new(roundto(lit(1.1), 1))
                .matches(Float, [1.1, 1.1, 1.1])
                .matches(Type::optional(Float), [Some(1.1), Some(1.1), Some(1.1)])
                .mismatches([String, Bool, Timestamp]),
            Case::new(round(lit(1.5)))
                .matches(Int, [2, 2, 2])
                .matches(Float, [2.0, 2.0, 2.0])
                .matches(Type::optional(Int), [Some(2), Some(2), Some(2)])
                .matches(Type::optional(Float), [Some(2.0), Some(2.0), Some(2.0)])
                .mismatches([String, Bool, Timestamp]),
            Case::new(roundto(lit(1.5), 0))
                .matches(Int, [2, 2, 2])
                .matches(Float, [2.0, 2.0, 2.0])
                .matches(Type::optional(Int), [Some(2), Some(2), Some(2)])
                .matches(Type::optional(Float), [Some(2.0), Some(2.0), Some(2.0)])
                .mismatches([String, Bool, Timestamp]),
            Case::new(roundto(lit(1.5), 1))
                .matches(Float, [1.5, 1.5, 1.5])
                .matches(Type::optional(Float), [Some(1.5), Some(1.5), Some(1.5)])
                .mismatches([String, Bool, Timestamp]),
            Case::new(round(lit(Value::None)))
                .matches(Type::optional(Int), [None::<Value>, None, None])
                .matches(Type::optional(Float), [None::<Value>, None, None])
                .mismatches([Int, Float, String, Bool, Timestamp]),
            Case::new(roundto(lit(Value::None), 1))
                .matches(Type::optional(Float), [None::<Value>, None, None])
                .mismatches([Int, Float, String, Bool, Timestamp]),
            // some columns
            Case::new(round(col("a")))
                .matches(Int, [1, 2, 3])
                .matches(Float, [1.0, 2.0, 3.0])
                .matches(Type::optional(Int), [Some(1), Some(2), Some(3)])
                .matches(Type::optional(Float), [Some(1.0), Some(2.0), Some(3.0)])
                .mismatches([String, Bool, Timestamp]),
            Case::new(roundto(col("a"), 1))
                .matches(Float, [1.0, 2.0, 3.0])
                .matches(Type::optional(Float), [Some(1.0), Some(2.0), Some(3.0)])
                .mismatches([String, Bool, Timestamp]),
            Case::new(round(col("c")))
                .matches(Int, [1, 2, 3])
                .matches(Float, [1.0, 2.0, 3.0])
                .matches(Type::optional(Int), [Some(1), Some(2), Some(3)])
                .matches(Type::optional(Float), [Some(1.0), Some(2.0), Some(3.0)])
                .mismatches([String, Bool, Timestamp]),
            Case::new(roundto(col("c"), 1))
                .matches(Float, [1.0, 2.0, 3.1])
                .matches(Type::optional(Float), [Some(1.0), Some(2.0), Some(3.1)])
                .mismatches([String, Bool, Timestamp]),
        ];
        check(df, cases);
    }

    #[test]
    fn test_abs() {
        let df = default_df();
        let cases = [
            Case::new(abs(lit(1)))
                .matches(Int, [1, 1, 1])
                .matches(Float, [1.0, 1.0, 1.0])
                .matches(Type::optional(Int), [Some(1), Some(1), Some(1)])
                .matches(Type::optional(Float), [Some(1.0), Some(1.0), Some(1.0)])
                .mismatches([String, Bool, Timestamp]),
            Case::new(abs(lit(-1)))
                .matches(Int, [1, 1, 1])
                .matches(Float, [1.0, 1.0, 1.0])
                .matches(Type::optional(Int), [Some(1), Some(1), Some(1)])
                .matches(Type::optional(Float), [Some(1.0), Some(1.0), Some(1.0)])
                .mismatches([String, Bool, Timestamp]),
            Case::new(abs(lit(1.1)))
                .matches(Float, [1.1, 1.1, 1.1])
                .matches(Type::optional(Float), [Some(1.1), Some(1.1), Some(1.1)])
                .mismatches([String, Bool, Timestamp]),
            Case::new(abs(lit(-1.1)))
                .matches(Float, [1.1, 1.1, 1.1])
                .matches(Type::optional(Float), [Some(1.1), Some(1.1), Some(1.1)])
                .mismatches([String, Bool, Timestamp]),
            Case::new(abs(lit(Value::None)))
                .matches(Type::optional(Int), [None::<Value>, None, None])
                .matches(Type::optional(Float), [None::<Value>, None, None])
                .mismatches([Int, Float, String, Bool, Timestamp]),
            // some columns
            Case::new(abs(col("a")))
                .matches(Int, [1, 2, 3])
                .matches(Float, [1.0, 2.0, 3.0])
                .matches(Type::optional(Int), [Some(1), Some(2), Some(3)])
                .matches(Type::optional(Float), [Some(1.0), Some(2.0), Some(3.0)])
                .mismatches([String, Bool, Timestamp]),
            Case::new(abs(col("c")))
                .matches(Float, [1.0, 2.0, 3.1])
                .matches(Type::optional(Float), [Some(1.0), Some(2.0), Some(3.1)])
                .mismatches([String, Bool, Timestamp]),
            Case::new(abs(col("h")))
                .matches(Float, [1.0, 2.0, 3.1])
                .matches(Type::optional(Float), [Some(1.0), Some(2.0), Some(3.1)])
                .mismatches([String, Bool, Timestamp]),
        ];
        check(df, cases);
    }

    #[test]
    fn test_struct_field_access_advanced() {
        // create customer df - with one struct column, one optional
        // struct column. Both structs should have an optional field
        let stype1 = Struct(Box::new(
            types::StructType::new(
                "stype1".into(),
                vec![
                    Field::new("int", Int),
                    Field::new("float", Float),
                    Field::new("string", String),
                    Field::new("optional_int", Type::optional(Int)),
                ],
            )
            .unwrap(),
        ));
        let stype2 = Type::optional(stype1.clone());
        let df = Dataframe::new(vec![
            Col::new(
                Arc::new(Field::new("a", stype1.clone())),
                Arc::new(vec![
                    Value::Struct(Arc::new(
                        value::Struct::new(vec![
                            ("int".into(), Value::Int(1)),
                            ("float".into(), Value::Float(1.0)),
                            ("string".into(), Value::String(Arc::new("hi".to_string()))),
                            ("optional_int".into(), Value::None),
                        ])
                        .unwrap(),
                    )),
                    Value::Struct(Arc::new(
                        value::Struct::new(vec![
                            ("int".into(), Value::Int(2)),
                            ("float".into(), Value::Float(2.0)),
                            ("string".into(), Value::String(Arc::new("bye".to_string()))),
                            ("optional_int".into(), Value::Int(3)),
                        ])
                        .unwrap(),
                    )),
                    Value::Struct(Arc::new(
                        value::Struct::new(vec![
                            ("int".into(), Value::Int(3)),
                            ("float".into(), Value::Float(3.0)),
                            (
                                "string".into(),
                                Value::String(Arc::new("something".to_string())),
                            ),
                            ("optional_int".into(), Value::Int(4)),
                        ])
                        .unwrap(),
                    )),
                ]),
            )
            .unwrap(),
            Col::new(
                Arc::new(Field::new("b", stype2.clone())),
                Arc::new(vec![
                    Value::Struct(Arc::new(
                        value::Struct::new(vec![
                            ("int".into(), Value::Int(1)),
                            ("float".into(), Value::Float(1.0)),
                            ("string".into(), Value::String(Arc::new("hi".to_string()))),
                            ("optional_int".into(), Value::None),
                        ])
                        .unwrap(),
                    )),
                    Value::None,
                    Value::Struct(Arc::new(
                        value::Struct::new(vec![
                            ("int".into(), Value::Int(3)),
                            ("float".into(), Value::Float(3.0)),
                            (
                                "string".into(),
                                Value::String(Arc::new("something".to_string())),
                            ),
                            ("optional_int".into(), Value::Int(4)),
                        ])
                        .unwrap(),
                    )),
                ]),
            )
            .unwrap(),
        ])
        .unwrap();
        let cases = [
            Case::new(col("a").dot("int")).produces(Int, [1, 2, 3]),
            Case::new(col("a").dot("float")).produces(Float, [1.0, 2.0, 3.0]),
            Case::new(col("a").dot("string")).produces(String, ["hi", "bye", "something"]),
            Case::new(col("a").dot("optional_int"))
                .produces(Type::optional(Int), [None, Some(3), Some(4)]),
            Case::new(col("b").dot("int")).produces(Type::optional(Int), [Some(1), None, Some(3)]),
            Case::new(col("b").dot("float"))
                .produces(Type::optional(Float), [Some(1.0), None, Some(3.0)]),
            Case::new(col("b").dot("string")).produces(
                Type::optional(String),
                [Some("hi"), None, Some("something")],
            ),
            Case::new(col("b").dot("optional_int"))
                .produces(Type::optional(Int), [None, None, Some(4)]),
            // invalid with missing field
            Case::new(col("a").dot("random")).invalid(),
            Case::new(col("b").dot("random")).invalid(),
        ];
        check(df, cases);
    }

    #[test]
    fn test_list_len() {
        let df = list_df();
        let cases = [
            Case::new(col("a").list_len()).produces(Int, [2, 1, 2]),
            Case::new(col("b").list_len()).produces(Type::optional(Int), [Some(2), None, Some(2)]),
            Case::new(col("c").list_len()).produces(Int, [3, 3, 3]),
            Case::new(col("d").list_len()).invalid(),
            Case::new(col("random").list_len()).invalid(),
            Case::new(lit(Value::None).list_len()).invalid(),
            Case::new(lit("hi").list_len()).invalid(),
        ];
        check(df, cases);
    }

    #[test]
    fn test_list_contains() {
        let df = list_df();
        let cases = [
            Case::new(col("a").list_has(lit(1))).produces(Bool, [true, false, false]),
            Case::new(col("a").list_has(lit(3))).produces(Bool, [false, true, false]),
            Case::new(col("a").list_has(lit(1.0))).invalid(),
            Case::new(col("a").list_has(lit("hi"))).invalid(),
            Case::new(col("a").list_has(lit(Value::None))).invalid(),
            Case::new(col("b").list_has(lit(1)))
                .produces(Type::optional(Bool), [Some(true), None, Some(false)]),
            Case::new(col("b").list_has(lit(Value::None))).invalid(),
            Case::new(col("c").list_has(lit(1))).produces(Type::optional(Bool), [Some(true), Some(false), None]),
            Case::new(col("c").list_has(lit(Value::None))).produces(Type::optional(Bool), [None::<Value>, None, None]),
            Case::new(col("e").list_has(lit(1)))
                .produces(Type::optional(Bool), [Some(true), None, Some(false)]),
        ];
        check(df, cases);
    }

    #[test]
    fn test_list_index_access() {
        let df = list_df();
        let cases = [
            Case::new(col("a").list_at(lit(Value::None))).invalid(),
            Case::new(col("a").list_at(lit(1.0))).invalid(),
            Case::new(col("a").list_at(lit(0)))
                .produces(Type::optional(Int), [Some(1), Some(3), Some(4)]),
            Case::new(col("a").list_at(lit(1)))
                .produces(Type::optional(Int), [Some(2), None, Some(5)]),
            Case::new(col("b").list_at(lit(0)))
                .produces(Type::optional(Int), [Some(1), None, Some(4)]),
            Case::new(col("b").list_at(lit(1)))
                .produces(Type::optional(Int), [Some(2), None, Some(5)]),
            Case::new(col("c").list_at(lit(0)))
                .produces(Type::optional(Int), [Some(1), Some(11), Some(3)]),
            Case::new(col("c").list_at(lit(1)))
                .produces(Type::optional(Int), [None, Some(Value::Int(4)), None]),
            Case::new(col("d").list_at(lit(0))).invalid(),
            Case::new(col("d").list_at(lit(1))).invalid(),
            Case::new(col("b").list_at(col("d")))
                .produces(Type::optional(Int), [Some(1), None, None]),
            // invalid with missing field
            Case::new(col("random").list_at(lit(2))).invalid(),
        ];
        check(df, cases);
    }

    #[test]
    fn test_struct_field_access() {
        let struct_lit = Value::Struct(Arc::new(
            value::Struct::new(vec![
                ("a".into(), Value::Int(1)),
                ("b".into(), Value::Float(1.0)),
                ("c".into(), Value::String(Arc::new("hi".to_string()))),
                ("d".into(), Value::Bool(true)),
                ("none".into(), Value::None),
            ])
            .unwrap(),
        ));
        let cases = [
            Case::new(lit(1).dot("a")).invalid(),
            Case::new(lit("hi").dot("a")).invalid(),
            Case::new(lit(Value::None).dot("a")).invalid(),
            Case::new(lit(true).dot("a")).invalid(),
            Case::new(lit(struct_lit.clone()).dot("a"))
                .matches(Int, [1, 1, 1])
                .matches(Type::optional(Int), [Some(1), Some(1), Some(1)])
                .matches(Float, [1.0, 1.0, 1.0])
                .matches(Type::optional(Float), [Some(1.0), Some(1.0), Some(1.0)])
                .mismatches([String, Bool, Timestamp]),
            Case::new(lit(struct_lit.clone()).dot("b"))
                .matches(Float, [1.0, 1.0, 1.0])
                .matches(Type::optional(Float), [Some(1.0), Some(1.0), Some(1.0)])
                .mismatches([Int, String, Bool, Timestamp]),
            Case::new(lit(struct_lit.clone()).dot("c"))
                .matches(String, ["hi", "hi", "hi"])
                .matches(Type::optional(String), [Some("hi"), Some("hi"), Some("hi")])
                .mismatches([Int, Float, Bool, Timestamp]),
            Case::new(lit(struct_lit.clone()).dot("d"))
                .matches(Bool, [true, true, true])
                .matches(Type::optional(Bool), [Some(true), Some(true), Some(true)])
                .mismatches([Int, Float, String, Timestamp]),
            Case::new(lit(struct_lit.clone()).dot("none"))
                .matches(Null, [None::<Value>, None, None])
                .matches(Type::optional(Int), [None::<Value>, None, None])
                .mismatches([Int, Float, String, Bool, Timestamp]),
            Case::new(lit(struct_lit.clone()).dot("random")).invalid(),
            // now with some columns
            Case::new(col("a").dot("int")).invalid(),
            Case::new(col("b").dot("int")).invalid(),
            Case::new(col("c").dot("int")).invalid(),
            Case::new(col("d").dot("int")).invalid(),
            Case::new(col("e").dot("int")).invalid(),
        ];
        check(default_df(), cases);
    }

    #[test]
    fn test_list_has_null() {
        // TODO: this doesn't work - fix
        let df = list_df();
        let cases = [
            Case::new(col("a").list_has_null()).produces(Bool, [false, false, false]),
            Case::new(col("b").list_has_null()).produces(Type::optional(Bool), [Some(false), None, Some(false)]),
            Case::new(col("c").list_has_null()).produces(Bool, [true, false, true]),
            Case::new(col("e").list_has_null()).produces(Type::optional(Bool), [Some(false), None, Some(false)]),
            Case::new(col("f").list_has_null()).produces(Type::optional(Bool), [Some(true), None, Some(true)]),
        ];
        check(df, cases);
    }

    #[test]
    fn test_str_length() {
        let df = default_df();
        let cases = [
            Case::new(lit(1).str_len()).invalid(),
            Case::new(lit(1.0).str_len()).invalid(),
            Case::new(lit(true).str_len()).invalid(),
            Case::new(lit("hi").str_len()).produces(Int, [2, 2, 2]),
            Case::new(col("a").str_len()).invalid(),
            Case::new(col("d").str_len()).produces(Int, [1, 3, 2]),
            Case::new(col("null_strings").str_len()).produces(Type::optional(Int), [Some(2), None, Some(3)]),
            Case::new(lit(Value::None).str_len()).produces(Type::optional(Int), [None::<Value>, None, None]),
        ];
        check(df, cases);
    }

    #[test]
    fn test_str_to_upper() {
        let df = default_df();
        let cases = [
            Case::new(lit(1).str_to_upper()).invalid(),
            Case::new(lit(1.0).str_to_upper()).invalid(),
            Case::new(lit(true).str_to_upper()).invalid(),
            Case::new(lit("hi").str_to_upper()).produces(String, ["HI", "HI", "HI"]),
            Case::new(col("a").str_to_upper()).invalid(),
            Case::new(col("d").str_to_upper()).produces(String, ["1", "1.0", "HI"]),
            Case::new(col("null_strings").str_to_upper()).produces(Type::optional(String), [Some("HI"), None, Some("BYE")]),
            Case::new(lit(Value::None).str_to_upper()).produces(Type::optional(String), [None::<Value>, None, None]),
        ];
        check(df, cases);
    }

    #[test]
    fn test_str_to_lower() {
        let df = default_df();
        let cases = [
            Case::new(lit(1).str_to_lower()).invalid(),
            Case::new(lit(1.0).str_to_lower()).invalid(),
            Case::new(lit(true).str_to_lower()).invalid(),
            Case::new(lit("Hi").str_to_lower()).produces(String, ["hi", "hi", "hi"]),
            Case::new(col("a").str_to_lower()).invalid(),
            Case::new(col("d").str_to_lower()).produces(String, ["1", "1.0", "hi"]),
            Case::new(col("null_strings").str_to_lower()).produces(Type::optional(String), [Some("hi"), None, Some("bye")]),
            Case::new(lit(Value::None).str_to_lower()).produces(Type::optional(String), [None::<Value>, None, None]),
        ];
        check(df, cases);
    }

    #[test]
    fn test_str_contains() {
        let df = default_df();
        let cases = [
            Case::new(lit(1).str_contains(lit("1"))).invalid(),
            Case::new(lit(1.0).str_contains(lit("1"))).invalid(),
            Case::new(lit(true).str_contains(lit("1"))).invalid(),
            Case::new(lit("1").str_contains(lit(1))).invalid(),
            Case::new(lit("Hello").str_contains(lit("ello"))).produces(Bool, [true, true, true]),
            Case::new(lit("Hello").str_contains(lit("yellow"))).produces(Bool, [false, false, false]),
            Case::new(lit("Hello").str_contains(lit(""))).produces(Bool, [true, true, true]),
            Case::new(lit("").str_contains(lit("yellow"))).produces(Bool, [false, false, false]),
            Case::new(lit("").str_contains(lit(""))).produces(Bool, [true, true, true]),
            Case::new(col("a").str_contains(lit("i"))).invalid(),
            Case::new(col("d").str_contains(lit("i"))).produces(Bool, [false, false, true]),
            Case::new(col("d").str_contains(lit("1"))).produces(Bool, [true, true, false]),
            Case::new(col("null_strings").str_contains(lit("i"))).produces(Type::optional(Bool), [Some(true), None, Some(false)]),
            Case::new(lit(Value::None).str_contains(lit(""))).produces(Type::optional(Bool), [None::<Value>, None, None]),

        ];
        check(df, cases);
    }

    #[test]
    fn test_str_starts_with() {
        let df = default_df();
        let cases = [
            Case::new(lit(1).str_starts_with(lit("1"))).invalid(),
            Case::new(lit(1.0).str_starts_with(lit("1"))).invalid(),
            Case::new(lit(true).str_starts_with(lit("1"))).invalid(),
            Case::new(lit("1").str_starts_with(lit(1))).invalid(),
            Case::new(lit("Hello").str_starts_with(lit("Hell"))).produces(Bool, [true, true, true]),
            Case::new(lit("Hello").str_starts_with(lit("Help"))).produces(Bool, [false, false, false]),
            Case::new(lit("Hello").str_starts_with(lit(""))).produces(Bool, [true, true, true]),
            Case::new(lit("").str_starts_with(lit("Help"))).produces(Bool, [false, false, false]),
            Case::new(lit("").str_starts_with(lit(""))).produces(Bool, [true, true, true]),
            Case::new(col("a").str_starts_with(lit("H"))).invalid(),
            Case::new(col("d").str_starts_with(lit("H"))).produces(Bool, [false, false, true]),
            Case::new(col("d").str_starts_with(lit("1"))).produces(Bool, [true, true, false]),
            Case::new(col("null_strings").str_starts_with(lit("H"))).produces(Type::optional(Bool), [Some(true), None, Some(false)]),
            Case::new(lit(Value::None).str_starts_with(lit(""))).produces(Type::optional(Bool), [None::<Value>, None, None]),
        ];
        check(df, cases);
    }

    #[test]
    fn test_str_ends_with() {
        let df = default_df();
        let cases = [
            Case::new(lit(1).str_ends_with(lit("1"))).invalid(),
            Case::new(lit(1.0).str_ends_with(lit("1"))).invalid(),
            Case::new(lit(true).str_ends_with(lit("1"))).invalid(),
            Case::new(lit("1").str_ends_with(lit(1))).invalid(),
            Case::new(lit("Hello").str_ends_with(lit("lo"))).produces(Bool, [true, true, true]),
            Case::new(lit("Hello").str_ends_with(lit("low"))).produces(Bool, [false, false, false]),
            Case::new(lit("Hello").str_ends_with(lit(""))).produces(Bool, [true, true, true]),
            Case::new(lit("").str_ends_with(lit("low"))).produces(Bool, [false, false, false]),
            Case::new(lit("").str_ends_with(lit(""))).produces(Bool, [true, true, true]),
            Case::new(col("a").str_ends_with(lit("i"))).invalid(),
            Case::new(col("d").str_ends_with(lit("i"))).produces(Bool, [false, false, true]),
            Case::new(col("d").str_ends_with(lit("1"))).produces(Bool, [true, false, false]),
            Case::new(col("null_strings").str_ends_with(lit("i"))).produces(Type::optional(Bool), [Some(true), None, Some(false)]),
            Case::new(lit(Value::None).str_ends_with(lit(""))).produces(Type::optional(Bool), [None::<Value>, None, None]),
        ];
        check(df, cases);
    }

    #[test]
    fn test_str_concat() {
        let df = default_df();
        let cases = [
            Case::new(lit(1).str_concat(lit("1"))).invalid(),
            Case::new(lit(1.0).str_concat(lit("1"))).invalid(),
            Case::new(lit(true).str_concat(lit("1"))).invalid(),
            Case::new(lit("1").str_concat(lit(1))).invalid(),
            Case::new(lit("foo").str_concat(lit(Value::None))).invalid(),
            Case::new(lit("Hel").str_concat(lit("lo"))).produces(String, ["Hello", "Hello", "Hello"]),
            Case::new(lit("Hell").str_concat(lit(""))).produces(String, ["Hell", "Hell", "Hell"]),
            Case::new(lit("").str_concat(lit("low"))).produces(String, ["low", "low", "low"]),
            Case::new(lit(Value::None).str_concat(lit("bar"))).produces(Type::optional(String), [None::<Value>, None, None]),
            Case::new(col("a").str_concat(lit("??"))).invalid(),
            Case::new(col("d").str_concat(lit("??"))).produces(String, ["1??", "1.0??", "Hi??"]),
            // TODO: This should produce [Some("Hi!!"), None, Some("Bye!!")]
            Case::new(col("null_strings").str_concat(lit("!!"))).produces(Type::optional(String), [Some("Hi!!"), Some("!!"), Some("Bye!!")]),
        ];
        check(df, cases);
    }

    fn round_trip(expr: Expr) -> Result<()> {
        let proto_expr: ProtoExpr = expr.clone().try_into()?;
        let new_expr: Expr = proto_expr.try_into()?;
        assert_eq!(expr, new_expr);
        Ok(())
    }

    #[test]
    fn test_ref() -> Result<()> {
        round_trip(Expr::Ref { name: "test".to_string() })
    }

    #[test]
    fn test_lit_serde() -> Result<()> {
        let value = Value::String(Arc::new("foo".into())); 
        let _ = round_trip(Expr::Lit { value });
        let _ = round_trip(Expr::Lit {value: Value::Int(123)});
        round_trip(Expr::Lit {value: Value::Float(123.0)})
    }

    #[test]
    fn test_unary() -> Result<()> {
        let _ = round_trip(Expr::Unary {
            op: UnOp::Not,
            expr: Box::new(Expr::Ref { name: "test".to_string() }),
        });
        let _ = round_trip(Expr::Unary { op: UnOp::Len, expr: Box::new(Expr::Ref { name: "test".to_string() }) });
        round_trip(Expr::Unary { op: UnOp::Neg, expr: Box::new(Expr::Lit { value: Value::Int(123) }) })
    }

    #[test]
    fn test_binary() -> Result<()> {
        round_trip(Expr::Binary {
            op: BinOp::Add,
            left: Box::new(Expr::Lit {
                value: Value::Int(12343) 
            }),
            right: Box::new(Expr::Lit {
                value: Value::Int(332)
            }),
        })
    }

    #[test]
    fn test_case() -> Result<()> {
        round_trip(Expr::Case {
            when_thens: vec![
                (
                    Expr::Binary {
                        op: BinOp::Eq,
                        left: Box::new(Expr::Ref { name: "a".to_string() }),
                        right: Box::new(Expr::Lit {
                            value: Value::Int(324) 
                        }),
                    },
                    Expr::Lit {
                        value: Value::Int(12) 
                    },
                ),
                (
                    Expr::Binary {
                        op: BinOp::Eq,
                        left: Box::new(Expr::Ref { name: "a".to_string() }),
                        right: Box::new(Expr::Lit {
                            value:  Value::String(Arc::new("foo".to_string())), 
                        }),
                    },
                    Expr::Lit {
                        value: Value::String(Arc::new("foo".to_string())), 
                    },
                ),
            ],
            otherwise: Some(Box::new(Expr::Lit {
                value: Value::Int(0) 
            })),
        })
    }

    #[test]
    fn test_is_null() -> Result<()> {
        round_trip(Expr::IsNull {
            expr: Box::new(Expr::Ref { name: "test".to_string() }),
        })
    }

    #[test]
    fn test_fill_null() -> Result<()> {
        round_trip(Expr::FillNull {
            expr: Box::new(Expr::Ref { name: "test".to_string() }),
            default: Box::new(Expr::Lit {
                value: Value::Int(0)
            }),
        })
    }

    #[test]
    fn test_math_fn() -> Result<()> {
        round_trip(Expr::MathFn {
            func: MathFn::Abs,
            expr: Box::new(Expr::Lit {
                value: Value::Int(0)
            }),
        })
    }

    #[test]
    fn test_string_fn() -> Result<()> {
        round_trip(Expr::StringFn {
            func: Box::new(StringFn::Len),
            expr: Box::new(Expr::Ref { name: "test".to_string() }),
        })
    }

    #[test]
    fn test_dict_fn() -> Result<()> {
        round_trip(Expr::DictFn {
            dict: Box::new(Expr::Ref { name: "test".to_string() }),
            func: Box::new(DictFn::Get {
                key: Expr::Lit {
                    value: Value::String(Arc::new("foo".to_string())), 
                },
                default: None,
            }),
        })
    }

    #[test]
    fn test_struct_fn() -> Result<()> {
        round_trip(Expr::StructFn {
            struct_: Box::new(Expr::Ref { name: "test".to_string() }),
            func: Box::new(StructFn::Get { field: "field".to_string() }),
        })
    }

    #[test]
    fn test_list_fn() -> Result<()> {
        round_trip(Expr::ListFn {
            list: Box::new(Expr::Ref { name: "test".to_string() }),
            func: Box::new(ListFn::Len),
        })
    }
}
