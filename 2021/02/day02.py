from typing import List
import sys
sys.path.insert(1, sys.path[0] + '/..')  # Add parent of my directory to path
import AOC  ## pylint: disable=import-error
lines: List = AOC.loadInput(None,'input')

TEST = ["forward 5", "down 5", "forward 8", "up 3","down 8", "forward 2"]

def part1(input: List) -> int:
    horizontal = 0
    depth = 0
    for data in input:
        cmd, length = data.split()
        length = int(length)
        if cmd == "forward":
            horizontal += length
        elif cmd == "down":
            depth += length
        elif cmd == "up":
            depth -= length
    return horizontal*depth

def part2(input: List) -> int:
    horizontal = 0
    depth = 0
    aim = 0
    for data in input:
        cmd, length = data.split()
        length = int(length)
        if cmd == "forward":
            horizontal += length
            depth += length*aim
        elif cmd == "down":
            aim += length
        elif cmd == "up":
            aim -= length
    return horizontal*depth

assert part1(TEST) == 150
assert part2(TEST) == 900
print("Part 1", part1(lines))
print("Part 2", part2(lines))
AOC.printTimeTaken()
