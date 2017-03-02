# The MIT License
#
#  Copyright (c) 2016, Oleg Nenashev and LibreCores contributors
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
LABEL Maintainer  Oleg Nenashev <o.v.nenashev@gmail.com>
LABEL Maintainer  Stefan Wallentowitz <stefan@wallentowitz.de>
LABEL Description "This is the default LibreCores CI Image"
LABEL Vendor      "Librecores"
LABEL Version     "2017.1"

USER root

RUN apt-get update
RUN apt-get install -y python environment-modules wget
RUN apt-get install -y python3 xdot graphviz
RUN apt-get install -y git mercurial subversion
RUN apt-get install -y python-dev python3-dev

# Install Java (required for using the image as Jenkins slave/agent)
RUN apt-get install -y openjdk-8-jre

# Mapping of Modules
VOLUME /tools
ENV MODULEPATH=/tools/modulefiles

WORKDIR /tmp
RUN wget https://bootstrap.pypa.io/get-pip.py
RUN python get-pip.py && rm get-pip.py
RUN pip install pytest tap.py

# Copy init files
#TODO: it seems the file is still unused
COPY bash.bashrc /etc/bash.bashrc

# Make bash the default shell instead of dash
# chsh is not an option since the user is being created randomly
RUN rm /bin/sh
RUN ["/bin/bash", "-c", "ln -s /bin/bash /bin/sh"]
RUN echo "DSHELL=/bin/bash" >> /etc/adduser.conf
