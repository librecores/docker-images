LibreCores CI Base Image for Docker
====

[![Docker Pulls](https://img.shields.io/docker/pulls/librecores/librecores-ci.svg)](https://hub.docker.com/r/librecores/librecores-ci/)

This is a base image which includes common EDA tools.

### Included tools

* [FuseSoC](https://fusesoc.net/) - Build system and EDA tool orchestration
* [Icarus Verilog](http://iverilog.icarus.com) - verilog simulation
* [Verilator](https://www.veripool.org/wiki/verilator) - verilog simulation
* [Yosys](http://www.clifford.at/yosys/) - for verilog synthesis
* [cocotb](https://github.com/potentialventures/cocotb) - write verilog testbenchs in python
* [pytest](https://docs.pytest.org/en/latest/) - generic python testing
  framework
* [tap.py](https://pypi.org/project/tap.py/) - python support for [TAP](http://testanything.org)

### Quick start 

Librecores CI docker image can be used in various projects which involves the use of various EDA 
toolsets and FuseSoC for testing and continuous integration. As an example Librecores-CI docker image 
is currently used in [OpenRISC](https://github.com/openrisc) projects such as
[mor1kx](https://github.com/openrisc/mor1kx) and [or1k_marocchino](https://github.com/openrisc/or1k_marocchino).

The [or1k Continuous Integration (CI) suite](https://github.com/openrisc/or1k-tests) is running in a 
Librecores-CI docker container in [Travis-CI](https://github.com/openrisc/mor1kx/blob/master/.travis.yml). 
Parallel execution of tests runs in Librecores-CI docker environment. As a reference one can follow
up the [blog](http://nancychauhan.in/stories/2019/06/08/gsoc-week1_2/) to get an idea of how
Librecores docker images can be integrated to existing continuous integration suite. 

#### Yosys Parser

[Yosys](http://www.clifford.at/yosys/) is a framework for Verilog RTL synthesis.
For monitoring resource usages of any hardware project, this parser script `extract-yosys-stats.py`
can help to visualise results better. This takes input from huge `yosys.log` file and outputs two
csv files.

##### yosys.log

Example input `yosys.log` log file.

```
47.28. Printing statistics.

=== mor1kx ===

   Number of wires:               5260
   Number of wire bits:          13413
   Number of public wires:         842
   Number of public wire bits:    8475
   Number of memories:               0
   Number of memory bits:            0
   Number of processes:              0
   Number of cells:               7213
     SB_CARRY                      430
     SB_DFF                        171
     SB_DFFE                       885
     SB_DFFESR                     569
     SB_DFFESS                      13
     SB_DFFSR                       48
     SB_DFFSS                        2
     SB_LUT4                      5084
     SB_RAM40_4K                    11
```

##### yosys-stats.csv 

This output file contains the top level the synthesis statistics.

```csv
wires,wire bits,public wires,public wire bits,memories,memory bits,processes,cells
5260,13413,842,8475,0,0,0,7213
```

##### yosys-cell-stats.csv

This output file contains a breakdown of the cell types.

```csv
SB_CARRY,SB_DFF,SB_DFFE,SB_DFFESR,SB_DFFESS,SB_DFFSR,SB_DFFSS,SB_LUT4,SB_RAM40_4K
430,171,885,569,13,48,2,5084,11
```

#### Quick Start 

One can see an example of the Yosys parser in [mor1kx](https://github.com/openrisc/mor1kx)
of the openrisc project.

One can also quickly get started with FuseSoC, a package manager and a set of build
tools for HDL (Hardware Description Language) code.
FuseSoC uses [edalize](https://github.com/olofk/edalize) which provides the icestorm backend.
The icestorm backend will invoke Yosys synthesis for a lattice FPGA.

1) Add the below to your core description file to enable yosys synthesis for your project. If you don't yet
have a FuseSoC core file you can can follow this
[quick tutorial](https://fusesoc.readthedocs.io/en/rtd/tutorials/tutorials.html) to get started.

```yml
 synth:
   default_tool : icestorm
   filesets : [X, Y]
   tools:
     icestorm:
       pnr: none
   toplevel : {XYZ}
 ```

2) Once modification in core file is done, you are set to run yosys synthesis in the
librecores/librecores-ci docker environment ( make sure to run the command in 
librecores/librecores-ci docker environment ), For example, for mor1kx following
commands are run to obtain printing statistics while running yosys synthesis :

```sh
fusesoc library add mor1kx /src
fusesoc run --target=synth mor1kx
test-scripts/extract-yosys-stats.py < build/mor1kx_*/synth-icestorm/yosys.log
```
