#!/usr/bin/env python
import os
import sys
with open(os.path.join(sys.path[0],'day04.data')) as fp:
   lines = [x.strip() for x in fp.readlines()]

reqfields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

def isvalidpassport(indict):
    count = 0
    for f in indict.keys():
        if f in reqfields:
            count += 1
    if count == 7:
        return True
    return False

new = 0
check = dict()
totalvalid = 0
for line in lines:
    if line == "":
        new = 1
        if isvalidpassport(check):
            totalvalid += 1
        check = dict()
    else:
        new = 0
        fields = line.split()
        for field in fields:
            (f,d) = field.split(':')
            check[f] = d
if isvalidpassport(check):
    totalvalid += 1

print(totalvalid)
