#!/usr/bin/env python
import sys
from collections import deque
from typing import List
t1 = [int(x) for x in list("389125467")]
data = [int(x) for x in list("974618352")]

""" Day 23: Crab Cups """

"""
Before the crab starts, it will designate the first cup in your list as the current cup.
The crab is then going to do 100 moves.

Each move, the crab does the following actions:

* The crab picks up the three cups that are immediately clockwise of the current cup.
    They are removed from the circle; cup spacing is adjusted as necessary to maintain the circle.
* The crab selects a destination cup:
  the cup with a label equal to the current cup's label minus one.
  If this would select one of the cups that was just picked up,
  the crab will keep subtracting one until it finds a cup that wasn't just picked up.
  If at any point in this process the value goes below the lowest value on any cup's label,
  it wraps around to the highest value on any cup's label instead.
* The crab places the cups it just picked up so that they are immediately clockwise of the destination cup.
  They keep the same order as when they were picked up.
* The crab selects a new current cup: the cup which is immediately clockwise of the current cup.
"""

def showcups(cups, pos):
    output = ""
    for i,a in enumerate(cups):
        if i == pos:
            output += f"({a}) "
        else:
            output += f" {a} "
    return output


def crabCups(cups: List[int], moves: int) -> List[int]:
    cuplen: int = len(cups)
    curpos: int = 0
    tmp: List[int] = list()
    cups2: List[int]
    for i in range(moves):
        cups2 = cups + cups
        current = cups[i%cuplen]
        print(f"-- move {i+1} --")
        print(f"cups: {showcups(cups,i%cuplen)}")
        tmp = cups[:]
        rem = [int(x) for x in cups2[curpos+1:curpos+4]]
        print(f"pick up: {showcups(rem,20)}")
        _ = [tmp.remove(a) for a in rem]
        dest = ((current-2)%cuplen)+1
        while dest in rem:
            # print(f"{dest=} {rem}")
            dest = ((dest-2)%cuplen)+1
        print(f"destination: {dest}")
        # print(f"PRE {current=} {dest=} {cups} {tmp=}")
        cups = tmp[0:tmp.index(dest)+1] + rem + tmp[tmp.index(dest)+1:][:cuplen]
        if (cups.index(dest) < curpos):
            # print('cupsrotate')
            cups =  (cups+cups)[cups.index(current)-curpos:cups.index(current)+cuplen-curpos]
        # print(f"POST {current=} {dest=} {cups} ")
        curpos = (curpos+1)%cuplen
        print("\n")
    return cups

final = crabCups(data,100)
print(f"-- final --\n{showcups(final,-1)}")
answer = "".join([str(x) for x in (final+final)[final.index(1)+1:final.index(1)+9]])
print(f"Answer: {answer}")