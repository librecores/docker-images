#! /bin/bash

cd /src

fusesoc library add mor1kx /src
fusesoc run --target=synth mor1kx
./extract_stats.py < build/mor1kx_5.0-r3/synth-icestorm/yosys.log
