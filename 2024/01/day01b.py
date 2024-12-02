#!/bin/python
import os
import sys
from pprint import pprint

filepath = (os.path.join(sys.path[0],"DATA"))

with open(filepath) as f:
    data = [l.rstrip("\n").split() for l in f.readlines()]

leftdata = [int(a[0]) for a in data]
rightdata = [int(a[1]) for a in data]

value = [a*rightdata.count(a) for a in leftdata]
print(sum(value))
