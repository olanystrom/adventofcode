#!/usr/bin/env python
import os
import sys
with open(os.path.join(sys.path[0],'day03.data')) as fp:
   lines = [x.strip() for x in fp.readlines()]

currentrow = 0
rows = len(lines[0])
tree = 0

def ishash(tecken):
    return "#" in tecken

for line in lines:
    if(ishash(line[currentrow%rows])):
        tree += 1
    currentrow += 3

print(f"{tree} trees")