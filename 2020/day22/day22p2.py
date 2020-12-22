#!/usr/bin/env python
import sys
from collections import deque
from copy import deepcopy
sys.path.insert(1, sys.path[0] + '/..')  # Add parent of my directory to path
import AOC  ## pylint: disable=import-error
lines = AOC.loadInput(None,'day22.data')

played = dict()
def is_played(level, p1, p2, c1, c2):
    if (level,c1,tuple(p1),c2,tuple(p2)) in played:
        print("Infinite recursion")
        print(f"{level,c1,tuple(p1),c2,tuple(p2)}")
        return True
    else:
        played[level,c1,tuple(p1),c2,tuple(p2)] = True
        return False

def parse_cards(lines):
    player = 0
    pCard = [None, None, None]
    pCard[1] = deque()
    pCard[2] = deque()
    for line in lines:
        if "Player" in line:
            player = int(line.split()[1][0])
            continue
        elif not line == "":
            pCard[player].append(int(line))
        else:
            pass
    return pCard

pCard = parse_cards(lines)

# print(f"Player 1 have: {len(pCard[1])} cards.")
# print(f"Player 2 have: {len(pCard[2])} cards.")
# print(f"Total of {len(pCard[1]) + len(pCard[2])} cards")

"""
Before either player deals a card, if there was a previous round in this game that had
    * exactly the same cards in the same order in the same players' decks, the game instantly ends in a win for player 1.
    Previous rounds from other games are not considered. (This prevents infinite games of Recursive Combat, which everyone agrees is a bad idea.)

Otherwise, this round's cards must be in a new configuration;
the players begin the round by each drawing the top card of their deck as normal.

* If both players have at least as many cards remaining in their deck as the value of the card they just drew,
the winner of the round is determined by playing a new game of Recursive Combat (see below).

* Otherwise, at least one player must not have enough cards left in their deck to recurse;
the winner of the round is the player with the higher-value card.
"""
gameid = 0
def get_gameid():
    global gameid
    gameid += 1
    return gameid

def recursive_combat(level, player1: deque, player2: deque):
    gid = get_gameid()
    p1 = deepcopy(player1)
    p2 = deepcopy(player2)
    print(f"level: {level:2d} Gid: {gameid}")
    # print(f"{'   ' * level }Player 1 have: {len(p1)} cards. {p1}")
    # print(f"{'   ' * level }Player 2 have: {len(p2)} cards. {p2}")
    # print(f"{'   ' * level }Total of {len(p1) + len(p2)} cards")
    while True:
        c1 = p1.popleft()
        c2 = p2.popleft()
        if is_played(gid, p1,p2, c1, c2):
            return 1,p1
        if c1 <= len(p1) and c2 <= len(p2):
            print(f"{'   ' * level}Starting Subgame {c1=} {c2=}")
            """To play a sub-game of Recursive Combat, each player creates a new deck by making a copy of the next cards in their deck
            (the quantity of cards copied is equal to the number on the card they drew to trigger the sub-game).
            """
            (winner, _) = recursive_combat(level+1, deque(list(p1)[0:c1]), deque(list(p2)[0:c2]))
            if winner == 1:
                p1.append(c1)
                p1.append(c2)
            else:
                p2.append(c2)
                p2.append(c1)
        else:
            # print(f"{'   ' * level}{p1=}")
            # print(f"{'   ' * level}{p2=}")
            if c1  > c2:
                # print(f"{'   ' * level}{c1=} > {c2=}")
                p1.append(c1)
                p1.append(c2)
            elif c2 > c1:
                # print(f"{'   ' * level}{c1=} < {c2=}")
                p2.append(c2)
                p2.append(c1)
            else:
                print("Lika")
        if len(p1) == 0:
            # print(f"{'   ' * level}Player 2 won")
            return(2, p2)
        elif len(p2) == 0:
            # print(f"{'   ' * level}Player 1 won")
            return(1, p1)

level = 1
winner, cards = recursive_combat(level, pCard[1], pCard[2]) 

ccount = len(cards)
score = 0
while len(cards) > 0:
    card = cards.popleft()
    print(f"{card=:2d} * {ccount=:2d} = {ccount*card}")
    score += ccount * card
    ccount -= 1
print(f"Score {score}")

AOC.printTimeTaken()