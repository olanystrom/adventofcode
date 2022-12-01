from typing import List
import sys
sys.path.insert(1, sys.path[0] + '/..')  # Add parent of my directory to path
import AOC  ## pylint: disable=import-error
lines: List = AOC.loadInput(None,'input.txt', notInt=True)
TEST: List = AOC.loadInput(None,'test.txt', notInt=True)

def part1(linput: List) -> int:
    maxelf, celf = 0, 0
    for line in linput:
        if len(line):
            celf += int(line)
        else:
            # print(maxelf)
            maxelf = max(celf, maxelf)
            celf = 0
    return maxelf


def part2(linput: List) -> int:
    celf =  0
    maxelf = list()
    for line in linput:
        if len(line):
            celf += int(line)
        else:
            maxelf.append(celf)
            # print(maxelf)
            celf = 0
    maxelf.append(celf)
    # print(maxelf)
    print(sorted(maxelf)[-3:])
    # print(sum(sorted(maxelf)[-3:]))
    return sum(sorted(maxelf)[-3:])


assert part1(TEST) == 24000
assert part2(TEST) == 45000
# print("Part 1 TEST", part1(TEST))
# print("Part 2 TEST", part2(TEST))
print("Part 1", part1(lines))
print("Part 2", part2(lines))
AOC.printTimeTaken()