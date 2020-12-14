#!/usr/bin/env python
import itertools
import sys
from bitstring import BitArray
sys.path.insert(1, sys.path[0] + '/..')  # Add parent of my directory to path
import AOC  ## pylint: disable=import-error
lines = AOC.loadInput(None,'day14.data')

class Memory():
    def _makemask(self, match, mask):
        _mask = BitArray(length=36)
        ci = -1
        while True:
            ci = mask.find(match,ci+1)
            if not ci == -1:
                _mask.set(1, pos=ci)
            else:
                return _mask

    def __init__(self, mask):
        self.mask1 = self._makemask('1', mask)
        self.mask0 = self._makemask('0', mask)
        self.maskx = self._makemask('X', mask)
        # print(f"1: {self.mask1.bin}")
        # print(f"0: {self.mask0.bin}")

    def makeadresses(self, adress):
        adress = int(adress) | self.mask1.uint
        adds = set()
        xes = [index for index, element in enumerate(self.maskx.bin) if element == '1']
        bits = BitArray(uint=adress, length=36)
        for sanning in itertools.product((True, False), repeat=len(xes)):
            for i,s in enumerate(sanning):
                # print(s,xes[i])
                bits.set(s, pos=xes[i])
                adds.add(bits.uint)
        return list(adds)


mem = dict()
for line in lines:
    if "mask" in line:
        Mask = Memory(line.split()[2])
    if "mem" in line:
        command, value = line.split('=')
        tmp1 = command.rindex('[')
        tmp2 = command.rindex(']')
        adress = command[tmp1+1:tmp2]
        adresses = Mask.makeadresses(adress)
        for a in adresses:
            mem[a] = int(value)
        # print(f"ad: {adress}")

print(sum(mem.values()))
AOC.printTimeTaken()
