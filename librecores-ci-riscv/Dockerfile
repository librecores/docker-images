# The MIT License
#
#  Copyright (c) 2017, Oleg Nenashev and LibreCores contributors
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in
#  all copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
#  THE SOFTWARE.

FROM librecores/librecores-ci:latest
LABEL maintainer "Oleg Nenashev <o.v.nenashev@gmail.com>"
LABEL maintainer "Stefan Wallentowitz <stefan@wallentowitz.de>"
LABEL Description="This is the default LibreCores CI Image for RISC-V builds" Vendor="Librecores" Version="2017.1"

USER root

# Compilers
# No releases/tags available, hence we just pick the fixed version
ARG RISCV_GNU_TOOLCHAIN_VERSION=ff21e26eb8c4d55dad7ad0b57e7bd8f7784a60e9

# RISC-V GNU Compiler Toolchain
WORKDIR /usr/src/riscv-gnu-toolchain
RUN apt-get install -y autoconf automake autotools-dev curl libmpc-dev libmpfr-dev libgmp-dev gawk build-essential bison flex texinfo gperf libtool patchutils bc zlib1g-dev
RUN git clone https://github.com/riscv/riscv-gnu-toolchain .
RUN git checkout ${RISCV_GNU_TOOLCHAIN_VERSION}
RUN git submodule update --init --recursive
# Currently we build the toolchain only for 32i. TODO: consider other architectures
RUN ./configure --prefix=/opt/riscv --with-arch=rv32i
RUN make linux
RUN make newlib
RUN ln -s /opt/riscv /opt/riscv32i

