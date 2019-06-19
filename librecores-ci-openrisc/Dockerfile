FROM librecores/librecores-ci:0.2.0

LABEL Description="This is the default LibreCores CI Image for openrisc builds" Vendor="Librecores" Version="2019.1"

WORKDIR /tmp/src/tools

RUN export TRAVIS_BUILD_DIR=/src 
RUN export HOME=/tmp

#Get toolchain
    
RUN apt-get update && apt-get install -y curl 
RUN apt install xz-utils
#RUN mkdir -p $HOME/src/tools \
#RUN mkdir -p $HOME/tools \
#RUN cd $HOME/src/tools && \
RUN curl --remote-name --location \
  https://github.com/stffrdhrn/gcc/releases/download/or1k-9.0.0-20181113/or1k-elf-9.0.0-20181112.tar.xz && tar -xvf or1k-elf-9.0.0-20181112.tar.xz

ENV PATH="$tmp/src/tools/or1k-elf/bin:${PATH}"

# Download and compile or1k-tests
#RUN cd $tmp/src/tools 
RUN git clone https://github.com/openrisc/or1k-tests.git ;
RUN cd or1k-tests/native 
RUN make -j2

# Setup fusesoc and add the cores required by or1k-tests
RUN fusesoc init -y 
RUN fusesoc library add mor1kx-generic https://github.com/stffrdhrn/mor1kx-generic.git 
RUN fusesoc library add intgen https://github.com/stffrdhrn/intgen.git 
RUN fusesoc library add mor1kx $TRAVIS_BUILD_DIR