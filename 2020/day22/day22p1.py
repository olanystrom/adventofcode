#!/usr/bin/env python
import sys
import queue
sys.path.insert(1, sys.path[0] + '/..')  # Add parent of my directory to path
import AOC  ## pylint: disable=import-error
lines = AOC.loadInput(None,'day22.data')

player = 0
pCard = [None, None, None]
pCard[1] = queue.Queue()
pCard[2] = queue.Queue()
for line in lines:
    if "Player" in line:
        player = int(line.split()[1][0])
        continue
    elif not line == "" :
        pCard[player].put(int(line))
    else:
        pass

print(f"Player 1 have: {pCard[1].qsize()} cards.")
print(f"Player 1 have: {pCard[2].qsize()} cards.")

count = 0
winner = 0
while True:
    c1 = pCard[1].get()
    c2 = pCard[2].get()
    count += 1
    if c1  > c2:
        print(f"{count:03d} {c1=} > {c2=}")
        pCard[1].put(c1)
        pCard[1].put(c2)
    elif c2 > c1:
        print(f"{count:03d} {c1=} < {c2=}")
        pCard[2].put(c2)
        pCard[2].put(c1)
    else:
        print("Lika")
    if pCard[1].empty():
        print("Player 2 won")
        winner = 2
        print(pCard[2])
        break
    elif pCard[2].empty():
        print("Player 1 won")
        winner = 1
        print(f"P1 have {pCard[1].qsize()} cards now")
        print(pCard[1])
        break

ccount = pCard[winner].qsize()
score = 0
while not pCard[winner].empty():
    card = pCard[winner].get()
    print(f"{card=:2d} * {ccount=:2d} = {ccount*card}")
    score += ccount * card
    ccount -= 1
print(f"Score {score}")
AOC.printTimeTaken()