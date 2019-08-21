#!/usr/bin/env python3
import sys
import re
import csv

def write_csv(file_path, content):
    with open(file_path, 'w') as csvFile:
        writer = csv.DictWriter(csvFile, content.keys())
        writer.writeheader()
        writer.writerow(content)


def main():
    parser_state = 0
    metrics = {}
    cells = {}

    # Printing statistics are extracted from yosys.log
    for line in sys.stdin:
        if parser_state == 0:
            if re.match(r"(?:\d+\.)* Printing statistics\.", line):
                parser_state = 1
        elif parser_state == 1:
            match_result = re.match(r"\s{3}Number of ([\w\s]+):\s+(\d+)", line)
            if match_result:
                metric = match_result.group(1)
                value = match_result.group(2)
                metrics[metric] = value

                if metric == "cells":
                    parser_state = 2
        elif parser_state == 2:
            match_result = re.match(r"\s{5}(\w+)\s+(\d+)", line)
            if match_result:
                cell_type = match_result.group(1)
                count = match_result.group(2)

                cells[cell_type] = count


    # Outputs the stats in CSV format
    write_csv('yosys-stats.csv', metrics)
    write_csv('yosys-cell-stats.csv', cells)


if __name__ == "__main__":
    main()
