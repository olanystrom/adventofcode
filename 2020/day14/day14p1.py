#!/usr/bin/env python
import itertools
import sys
from bitstring import BitArray
sys.path.insert(1, sys.path[0] + '/..')  # Add parent of my directory to path
import AOC  ## pylint: disable=import-error
lines = AOC.loadInput(None,'day14.data')


class Memory():
    def _makemask1(self, mask):
        _mask = BitArray(length=36)
        ci = -1
        while True:
            ci = mask.find('1',ci+1)
            if not ci == -1:
                _mask.set(1, pos=ci)
            else:
                return _mask

    def _makemask0(self, mask):
        _mask = BitArray(length=36)
        ci = -1
        while True:
            ci = mask.find('0',ci+1)
            if not ci == -1:
                _mask.set(1, pos=ci)
            else:
                return _mask

    def __init__(self, mask):
        self.mask1 = self._makemask1(mask)
        self.mask0 = self._makemask0(mask)
        # print(f"1: {self.mask1.bin}")
        # print(f"0: {self.mask0.bin}")

    def setmasked(self, value):
        onecomplement = int(value) | self.mask1.uint
        zeroes = [index for index, element in enumerate(self.mask0.bin) if element == '1']
        bits = BitArray(uint=onecomplement, length=36)
        bits.set(0, pos=zeroes)
        return bits.uint

mem = dict()
for line in lines:
    if "mask" in line:
        Mask = Memory(line.split()[2])
    if "mem" in line:
        command, value = line.split('=')
        tmp1 = command.rindex('[')
        tmp2 = command.rindex(']')
        adress = command[tmp1+1:tmp2]
        # print(f"ad: {adress}")
        mem[adress] = Mask.setmasked(value)

# for k in mem:
#     print(k,mem[k])

print(sum(mem.values()))
AOC.printTimeTaken()



"""  with 1
1010
1100
0010
"""

"""  with 0
1010
0011
0011
"""