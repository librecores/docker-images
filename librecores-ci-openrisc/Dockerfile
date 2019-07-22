FROM librecores/librecores-ci:0.2.0

LABEL Description="This is the default LibreCores CI Image for openrisc builds" Vendor="Librecores" Version="2019.1"

WORKDIR /tmp/src/tools
RUN export HOME=/tmp

#Get toolchain
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
RUN make -j8                                          