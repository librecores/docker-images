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
* Yosys Parser 

### Quick start 

Librecores CI docker image can be used in various projects which involves the use of various EDA 
toolsets and Fusesoc for testing and continous integration. As an example Librecores-CI docker image 
is currently used in [OpenRisc](https://github.com/openrisc) projects such as [mor1kx](https://github.com/openrisc/mor1kx) and [or1k_marocchino](https://github.com/openrisc/or1k_marocchino).

The [or1k Continuous Integration (CI) suite](https://github.com/openrisc/or1k-tests) is running in a 
Librecores-CI docker container in [Travis-CI](https://github.com/openrisc/mor1kx/blob/master/.travis.yml). 
Parallel execution of tests runs in Librecores-CI docker environment. As a reference one can follow up the [blog](http://nancychauhan.in/stories/2019/06/08/gsoc-week1_2/) to get an idea of how librecores docker images can be 
integrated to existing continuous integration suite. 

#### Yosys Parser
Yosys is a framework for Verilog RTL synthesis. For monitoring resource usages of any hardware project, this parser script (extract-yosys-stats.py) can help to visualise results better. This take input from huge yosys.log file and outputs 'Printing Statistics' like :
```
wire bits,16199
public wires,1058
public wire bits,11151
memories,0
memory bits,0
processes,0
cells,7310
SB_CARRY,426
SB_DFF,166
SB_DFFE,885
SB_DFFESR,569
SB_DFFESS,13
SB_DFFSR,56
SB_DFFSS,2
SB_LUT4,5182
SB_RAM40_4K,11
```

#### Quick Start 

To use Yosys Parser, you can see its implementation in <a href="https://github.com/openrisc/mor1kx">openrisc project<a>.

One can quickly get started with Fusesoc, a package manager and a set of build tools for HDL (Hardware Description Language) code.
Fusesoc provides the <a href = "https://github.com/olofk/edalize">icestorm backend</a> ( edalize ) which uses yosys to handle synthesis, arachne-pnr for place & route and icepack for creating the bitstream.
1) Do changes in core description file to support icestorm for your project. One can follow <a href="https://fusesoc.readthedocs.io/en/rtd/fusesoc.html"> quick tutorial <a>for writing a core description file. Example:
```
 synth:
 default_tool : icestorm
 filesets : [X, Y]
 tools:
 icestorm:
 pnr: none
 toplevel : {XYZ}
 ```

2) Once modification in core file is done, you are set to run yosys synthesis in librecores/librecores-ci docker environment
( make sure to run the command in librecores/librecores-ci docker environment ), For example, for mor1kx following commands are run to obtain printing statistics while running yosys synthesis :
```
fusesoc library add mor1kx /src
fusesoc run --target=synth mor1kx
test-scripts/extract-yosys-stats.py < build/mor1kx_*/synth-icestorm/yosys.log
```
