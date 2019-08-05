FROM librecores/librecores-ci:0.3.0

LABEL Description="This is the default LibreCores CI Image for openrisc builds" Vendor="Librecores" Version="2019.1"

WORKDIR /tmp/src/tools
RUN export HOME=/tmp

# No releases/tags available, hence we just pick the fixed verion
ARG OR1K_TESTS_VERSION=7372eae64b2f25cffaac7792fe2bc918919061bf

# Get toolchain
RUN apt-get update && apt-get install -y curl
RUN apt install xz-utils
RUN curl --remote-name --location \
  https://github.com/stffrdhrn/gcc/releases/download/or1k-9.0.0-20181113/or1k-elf-9.0.0-20181112.tar.xz
RUN mkdir -p /tmp/tools
RUN tar xC /tmp/tools -f  or1k-elf-9.0.0-20181112.tar.xz

ENV PATH="/tmp/tools/or1k-elf/bin:${PATH}"

# Download and compile or1k-tests
RUN git clone https://github.com/openrisc/or1k-tests.git 
WORKDIR /tmp/src/tools/or1k-tests/native
RUN git checkout ${OR1K_TESTS_VERSION}
RUN make -j8                                          
