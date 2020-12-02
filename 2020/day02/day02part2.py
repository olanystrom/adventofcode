#!/usr/bin/env python
from functools import lru_cache
import os
import sys
with open(os.path.join(sys.path[0],'day02.data')) as fp:
   lines = fp.readlines()


@lru_cache(maxsize=256)
def validpass(line):
    # format 8-9 x: xxxxxxxrk
    (code, password) = line.split(':')
    (num, tecken) = code.split(' ')
    (low,high) = [int(x) for x in num.split('-')]
    passwordlist = list(password)
    first = passwordlist[low] == tecken
    second = passwordlist[high] == tecken
    return (first ^ second)

validcount = 0
for line in lines:
    if validpass(line):
        validcount += 1
print(f"Total valid: {validcount}")