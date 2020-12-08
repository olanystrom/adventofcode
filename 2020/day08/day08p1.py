#!/usr/bin/env python
import os
import sys
with open(os.path.join(sys.path[0],'day08.data')) as fp:
   lines = [x.strip() for x in fp.readlines()]


currentline = 0
acc = 0
visitedlines = set()
while True:
    (command, arg) = lines[currentline].split()
    if currentline in visitedlines:
        print(acc)
        break
    visitedlines.add(currentline)
    if command == "acc":
        acc += int(arg)
        currentline += 1
    elif command == "nop":
        currentline += 1
    elif command == "jmp":
        currentline += int(arg)
    else:
        print(f"Unexpected command {command}")
        break