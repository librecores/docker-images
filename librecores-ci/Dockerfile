# The MIT License
#
#  Copyright (c) 2016, Oleg Nenashev
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

FROM ubuntu:16.04
LABEL maintainer "Oleg Nenashev <o.v.nenashev@gmail.com>"
LABEL maintainer "Stefan Wallentowitz <stefan@wallentowitz.de>"
LABEL Description="This is the default LibreCores CI Image" Vendor="Librecores" Version="2017.1"

USER root

# Package Managers
ARG FUSESOC_VERSION=1.9

# Simulation
ARG ICARUS_VERILOG_VERSION=10_2
ARG VERILATOR_VERSION=4.014

# Synthesis
ARG YOSYS_VERSION=0.8

# Testing
ARG COCOTB_VERSION=1.5
ARG PYTEST_VERSION=4.5.0
ARG TAPPY_VERSION=2.5

RUN apt-get update && apt-get install -y \
    python2.7-dev libyaml-dev libyaml-dev python-pip python-yaml git libelf-dev \
    autoconf gperf bison flex build-essential clang libreadline-dev gawk tcl-dev \
    libffi-dev mercurial graphviz xdot pkg-config python3

# FuseSoC
ENV FUSESOC_VERSION=${FUSESOC_VERSION}

WORKDIR /usr/src/fusesoc
RUN git clone https://github.com/olofk/fusesoc.git .
RUN git checkout ${FUSESOC_VERSION}
RUN pip install -e .

# Icarus Verilog
ENV ICARUS_VERILOG_VERSION=${ICARUS_VERILOG_VERSION}

WORKDIR /usr/src/iverilog
RUN git clone https://github.com/steveicarus/iverilog.git .
RUN git checkout v${ICARUS_VERILOG_VERSION}
RUN sh autoconf.sh
RUN ./configure
RUN make
RUN make install

# Verilator
ENV VERILATOR_VERSION=${VERILATOR_VERSION}

WORKDIR /usr/src/verilator
RUN git clone http://git.veripool.org/git/verilator .
RUN git checkout verilator_`echo "${VERILATOR_VERSION}" | tr '.' '_'`
RUN autoconf
RUN ./configure
RUN make
RUN make install

# Yosys
WORKDIR /usr/src/yosys
RUN git clone http://github.com/cliffordwolf/yosys.git .
RUN git checkout yosys-${YOSYS_VERSION}
RUN make config-gcc
RUN make
RUN make install

# test-scipts:extract-yosys-stats.py outputs 'Printing Statistics' for monitoring resource usages by running yosys synthesis.
COPY test-scripts /test-scripts 

# pytest, nose and tappy
RUN pip install pytest==${PYTEST_VERSION}
RUN pip install tap.py==${TAPPY_VERSION}
