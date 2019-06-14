LibreCores CI Base Image for Docker
====

[![Docker Pulls](https://img.shields.io/docker/pulls/librecores/librecores-ci.svg)](https://hub.docker.com/r/librecores/librecores-ci/)

This is a base image which includes common EDA tools.

### Included tools

* FuseSoC
* Icarus Verilog
* Verilator
* Yosys
* [cocotb](https://github.com/potentialventures/cocotb)
* [pytest](https://docs.pytest.org/en/latest/)
* [tap.py](https://pypi.org/project/tap.py/)

### Quick start 

Librecores_CI docker image can be used in various projects which involves the use of various EDA 
toolsets and Fusesoc for testing and continous integration. As an example Librecores-CI docker image 
is currently used in [OpenRisc](https://github.com/openrisc) projects such as [mor1kx](https://github.com/openrisc/mor1kx) and 
[or1k_marocchino](https://github.com/openrisc/or1k_marocchino).

The [or1k Continuous Integration (CI) suite](https://github.com/openrisc/or1k-tests) is running in a 
Librecores-CI docker container in [Travis CI](https://github.com/openrisc/mor1kx/blob/master/.travis.yml). 
Parallel execution of tests runs in Librecores-CI docker environment. Librecores-CI 
image includes the installation of common EDA tools such as Icarus Verilog, Verilator and Yosys that 
is required by CI suite for testing.

