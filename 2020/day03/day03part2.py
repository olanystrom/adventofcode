#!/usr/bin/env python
import os
import sys
with open(os.path.join(sys.path[0],'day03.data')) as fp:
   lines = [x.strip() for x in fp.readlines()]

def ishash(tecken):
    return "#" in tecken

def rd(lines, right, down):
    currentrow = 0
    rows = len(lines[0])
    tree = 0

    if down == 1:
        for line in lines:
            if(ishash(line[currentrow%rows])):
                tree += 1
            currentrow += right
    elif down == 2:
        for num,line in enumerate(lines):
            if not num%2:
                # print(f"{num}")
                if(ishash(line[currentrow%rows])):
                    tree += 1
                currentrow += right
    else:
        print('ERR')
    return tree

print(rd(lines,1,1)*rd(lines,3,1)*rd(lines,5,1)*rd(lines,7,1)*rd(lines,1,2))