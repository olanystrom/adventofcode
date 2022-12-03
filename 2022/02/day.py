from typing import List
import sys
sys.path.insert(1, sys.path[0] + '/..')  # Add parent of my directory to path
import AOC  ## pylint: disable=import-error
lines: List = AOC.loadInput(None,'input', notInt=True)
TEST: List = AOC.loadInput(None,'test', notInt=True)

def part1(linput: List) -> int:
   return 0


def part2(linput: List) -> int:
   return 0


# assert part1(TEST) == 198
# assert part2(TEST) == 230
# print("Part 1 TEST", part1(TEST))
# print("Part 2 TEST", part2(TEST))
# print("Part 1", part1(lines))
# print("Part 2", part2(lines))
AOC.printTimeTaken()
