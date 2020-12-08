#!/usr/bin/env python
from functools import lru_cache
import os
import sys
with open(os.path.join(sys.path[0],'day07.data')) as fp:
   lines = [x.strip() for x in fp.readlines()]

def canhold(innerbag, bags):
    answer = list()
    for bag in bags:
        for bg in bags[bag]:
            if innerbag in bg:
                answer.append(bag)
    return answer


bags = dict()
MYBAG = "shiny gold"

for line in lines:
    """ light red bags contain 1 bright white bag, 2 muted yellow bags. """
    outerbag = " ".join(line.split()[0:2])   # First two words
    innerbags = " ".join(line.split()[4:]).split(',')  # list of inner bags
    bags[outerbag] = innerbags


count = 0
# count += MYBAG in bags.keys()    
cbags = canhold(MYBAG,bags)
seenbags = set(cbags)
while len(cbags) > 0:
    nbags = list()
    print(cbags)
    for cb in cbags:
        seenbags.add(cb)
        if(len(canhold(cb, bags))):
            nbags.extend(canhold(cb, bags))
    cbags = list(set(nbags))
print(len(seenbags))