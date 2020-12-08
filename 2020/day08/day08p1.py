#!/usr/bin/env python
import sys
sys.path.insert(1, sys.path[0] + '/..')  # Add parent of my directory to path
import AOC
lines = AOC.loadInput(8)

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

AOC.printTimeTaken()