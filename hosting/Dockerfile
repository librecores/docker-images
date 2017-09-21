FROM ubuntu:16.04
LABEL maintainer "Stefan Wallentowitz <stefan@fossi-foundation.org>"

RUN apt-get update && apt-get install -y libffi-dev python3 python3-venv ruby ruby-bundler ruby-dev git
RUN gem install bundler
WORKDIR /tmp
