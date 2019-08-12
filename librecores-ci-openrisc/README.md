LibreCores CI image for OpenRISC development
============================================

[![Docker Pulls](https://img.shields.io/docker/pulls/librecores/librecores-ci-openrisc.svg)](https://hub.docker.com/r/librecores/librecores-ci-openrisc/)

Librecores CI image for OpenRISC development is based on the standard [Librecores-CI](https://github.com/librecores/docker-images/tree/master/librecores-ci) docker image and it largely targets the [FuseSoC](https://github.com/olofk/fusesoc) use cases. This image mainly focuses on [OpenRISC](https://github.com/openrisc) project that creates a free and open processor for embedded systems.

 ### Quick Start

Currently librecores-ci-openrisc is successfully implemented in [mor1kx](https://github.com/openrisc/mor1kx) and [or1k-marocchino](https://github.com/Nancy-Chauhan/or1k_marocchino) projects.

The [or1k Continuous Integration (CI)](https://github.com/openrisc/or1k-tests) suite is running in a librecores-ci-openrisc docker container in Travis CI. Parallel execution of tests runs in librecores-ci-openrisc docker environment.

The librecores-ci base image includes installation of common EDA tools such as Icarus Verilog, Verilator and Yosys that is required by CI suite in openrisc projects for testing. librecores/libreocres-ci-openrisc docker image gets the toolchain required, downloads and compiles the or1k-tests.
