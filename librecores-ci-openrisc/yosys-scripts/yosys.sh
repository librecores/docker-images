#! /bin/bash

set -x
cd /src

fusesoc library add $TOPLEVEL /src
fusesoc run --target=synth $TOPLEVEL
/test-scripts/extract-yosys-stats.py  < build/${TOPLEVEL}_${VERSION}/synth-icestorm/yosys.log
