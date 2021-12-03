from typing import List
import sys
sys.path.insert(1, sys.path[0] + '/..')  # Add parent of my directory to path
import AOC  ## pylint: disable=import-error
lines: List = AOC.loadInput(None,'input', notInt=True)

TEST = ["00100", "11110", "10110", "10111",
        "10101", "01111", "00111", "11100",
        "10000","11001","00010", "01010" ]

def part1(input: List) -> int:
    bits = [int(a) for a in "0" * len(str(input[0]))] 
    sbits = [int(a) for a in "0" * len(str(input[0]))] 
    ubits = [int(a) for a in "0" * len(str(input[0]))] 
    for line in input:
        for n,bit in enumerate(str(line)):
            bits[n] += int(bit)
    half = len(input)/2
    for n,a in enumerate(bits):
        if a > half:
            sbits[n] = 1
            ubits[n] = 0
        else:
            sbits[n] = 0
            ubits[n] = 1
    gamma = int("".join([str(a) for a in sbits]),2)
    epsilon = int("".join([str(a) for a in ubits]),2)    
    print(sbits, gamma)
    print(ubits, epsilon)
    return gamma*epsilon



def part2(linput: List) -> int:
    oxylist = linput.copy()
    co2list = linput.copy()
    oxycompare = []
    co2compare = []
    for n in range(len(linput[0])):
    
        if sum([int(a[n:n+1]) for a in oxylist]) >= len(oxylist)/2:
            oxycompare.append('1')
        else:
            oxycompare.append('0')
    
        if sum([int(a[n:n+1]) for a in co2list]) >= len(co2list)/2:
            co2compare.append('0')
        else:
            co2compare.append('1')
    
        oxylist = [a for a in oxylist if list(a[:n+1]) == oxycompare]
        co2list = [a for a in co2list if list(a[:n+1]) == co2compare]
    
        if len(oxylist) == 1:
            oxygen = int("".join([str(a) for a in oxylist]),2)
        if len(co2list) == 1:
            co2 = int("".join([str(a) for a in co2list]),2)
    return oxygen*co2

assert part1(TEST) == 198
assert part2(TEST) == 230
# print("Part 1 TEST", part1(TEST))
# print("Part 2 TEST", part2(TEST))
print("Part 1", part1(lines))
print("Part 2", part2(lines))
AOC.printTimeTaken()
