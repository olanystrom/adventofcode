#!/usr/bin/env python
import os
import sys
with open(os.path.join(sys.path[0],'day08.data')) as fp:
   lines = [x.strip() for x in fp.readlines()]

def bootsuccess():
    currentline = 0
    totallines = len(lines)
    acc = 0; visitedlines = set()
    while True:
        if(currentline == totallines):
            print(f"Success: {acc}")
            return True
        if currentline in visitedlines:
            # print(f"fail at line: {currentline} with acc: {acc}")
            return False
        visitedlines.add(currentline)
        (command, arg) = lines[currentline].split()
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

if bootsuccess():
    end()

for (num,line) in enumerate(lines):
    (command, arg) = line.split()
    if command == "nop":
        lines[num] = f"jmp {arg}"
        if bootsuccess():
            print(f"jmp at line: {num}")
            break
        lines[num] = f"nop {arg}"
    elif command == "jmp":
        lines[num] = f"nop {arg}"
        if bootsuccess():
            print(f"jmp at line: {num}")
            break
        lines[num] = f"jmp {arg}"
