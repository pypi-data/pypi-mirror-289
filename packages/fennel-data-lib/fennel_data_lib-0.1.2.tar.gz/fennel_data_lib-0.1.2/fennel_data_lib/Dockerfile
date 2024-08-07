# Use the PyO3/Maturin base image
FROM ghcr.io/pyo3/maturin

RUN dnf install -y epel-release
RUN dnf install -y --nogpgcheck https://download1.rpmfusion.org/free/el/rpmfusion-free-release-8.noarch.rpm
RUN dnf install -y --nogpgcheck https://download1.rpmfusion.org/nonfree/el/rpmfusion-nonfree-release-8.noarch.rpm
RUN dnf install -y ffmpeg ffmpeg-devel
RUN dnf install -y clang clang-devel

# add manylinux python interpreters we need
#
ENV PATH="/root/.cargo/bin:/opt/python/cp37-cp37m/bin:/opt/python/cp38-cp38/bin:/opt/python/cp39-cp39/bin:/opt/python/cp310-cp310/bin:/opt/python/cp311-cp311/bin:/opt/python/cp312-cp312/bin:$PATH"

# maturin installation
#
RUN pip3 install maturin==0.15 patchelf cffi ziglang sccache>=0.4.0

# install Rust
WORKDIR /opt
COPY docker/install-basic-deps-manylinux.sh .
RUN bash /opt/install-basic-deps-manylinux.sh

# Our base image with Rust, Maturin, and system dependencies
#
FROM base as chef
ENV PATH="/root/.cargo/bin:$PATH"
RUN rustc -V



