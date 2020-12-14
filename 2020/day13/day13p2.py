#!/usr/bin/env python
import itertools
import sys
import math
from functools import reduce
sys.path.insert(1, sys.path[0] + '/..')  # Add parent of my directory to path
import AOC  ## pylint: disable=import-error
lines = AOC.loadInput(None,'day13.data')

times = lines[1].split(',')

#Bruteforcetime
# >>> gcd(3420,19)
# 19
# >>> gcd(3419,13)
# 13
# >>> gcd(3417,17)
# 17


maxnum = sorted([int(x) for x in times if x.isdigit()])

nogcd = False
cmp = maxnum[-1]
maxstep = reduce((lambda x, y: x * y), maxnum)
print(cmp, maxstep)
while True:
    for i,a in enumerate(times):
        if a == 'x' or nogcd:
            next
        elif math.gcd(cmp+i, int(a)) == int(a):
            if i > 11:
                print(i, cmp+i,a)
            next
        else:
            nogcd = True
    if nogcd is False:
        print("Found", i, a)
        exit()
    nogcd = False
    cmp += maxnum[-1]            