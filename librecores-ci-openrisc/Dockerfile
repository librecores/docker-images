FROM librecores/librecores-ci:latest

LABEL Description="This is the default LibreCores CI Image for openrisc builds" Vendor="Librecores" Version="2019.1"

#Get toolchain
RUN mkdir -p $HOME/src/tools \
    mkdir -p $HOME/tools \
    cd $HOME/src/tools \
    export TRAVIS_BUILD_DIR=/src

RUN apt-get update && apt-get install -y curl 

RUN curl --remote-name --location \
  https://github.com/stffrdhrn/gcc/releases/download/or1k-9.0.0-20181113/or1k-elf-9.0.0-20181112.tar.xz 
RUN  tar xC $HOME/tools -f $HOME/src/tools/or1k-elf-9.0.0-20181112.tar.xz

ENV PATH="$HOME/tools/or1k-elf/bin:${PATH}"

# Download and compile or1k-tests
RUN cd $HOME/src/tools && \
git clone https://github.com/openrisc/or1k-tests.git ; &&\
cd or1k-tests/native \
make -j2

# Setup fusesoc and add the cores required by or1k-tests
RUN fusesoc init -y \
fusesoc library add mor1kx-generic https://github.com/stffrdhrn/mor1kx-generic.git \
fusesoc library add intgen https://github.com/stffrdhrn/intgen.git \
fusesoc library add mor1kx $TRAVIS_BUILD_DIR