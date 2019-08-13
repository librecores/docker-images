#!/usr/bin/env python3
import sys
import re
import csv

parser_state = 0
matches = []
cells = []

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
            matches.append((metric, value))

            if metric == "cells":
                parser_state = 2
    elif parser_state == 2:
        match_result = re.match(r"\s{5}(\w+)\s+(\d+)", line)
        if match_result:
            cell_type = match_result.group(1)
            count = match_result.group(2)

            cells.append((cell_type, count))

print(matches)
print(cells)

# Outputs the stats in CSV format
with open('result.csv', 'w') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerows(matches)
    writer.writerows(cells)

with open('result.csv', newline='') as f:
    r = csv.reader(f)
    data = [line for line in r]
with open('result.csv', 'w', newline='')as f:
    w = csv.writer(f)
    w.writerow(['label', 'elapsed'])
    w.writerows(data)

# Code for getting JMeter compatible CSV file for Performance Plugin
# TODO: result.csv with Key Value has to be made compatible with Jenkins Perforamce plugin
in_file = 'result.csv'
out_file = 'report.csv'
with open(in_file, 'r') as in_f, open(out_file, 'w', newline='') as out_f:
    rdr = csv.DictReader(in_f)
    fieldnames = ['timeStamp', 'responseCode', 'responseMessage',
                  'threadName', 'dataType', 'success', 'bytes']
    fieldnames.extend(rdr.fieldnames)
    wrtr = csv.DictWriter(out_f, fieldnames=fieldnames)
    wrtr.writeheader()
    for row_id, row in enumerate(rdr, start=1):
        row['timeStamp'] = '2019-08-14 14:15:25.321'.format(row_id)
        row['responseCode'] = '200'.format(row_id)
        row['responseMessage'] = 'OK'.format(row_id)
        row['threadName'] = 'Thread Group 1-1'.format(row_id)
        row['dataType'] = 'text'.format(row_id)
        row['success'] = 'true'.format(row_id)
        row['bytes'] = '3478'.format(row_id)
        wrtr.writerow(row)

with open('report.csv', 'r') as infile, open('output.csv', 'a') as outfile:
    fieldnames = ['timeStamp', 'elapsed', 'label', 'responseCode',
                  'responseMessage', 'threadName', 'dataType', 'success', 'bytes']
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    writer.writeheader()
    for row in csv.DictReader(infile):
        writer.writerow(row)
