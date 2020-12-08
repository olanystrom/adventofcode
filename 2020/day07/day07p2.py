#!/usr/bin/env python
import os
import sys
with open(os.path.join(sys.path[0],'day07.data')) as fp:
   lines = [x.strip() for x in fp.readlines()]

bags = dict()
MYBAG = "shiny gold"

for line in lines:
    """ light red bags contain 1 bright white bag, 2 muted yellow bags. """
    outerbag = " ".join(line.split()[0:2])   # First two words
    innerbags = " ".join(line.split()[4:]).split(',')  # list of inner bags
    bags[outerbag] = [b.lstrip() for b in innerbags]

""" shiny gold bags contain 1 dim lavender bag, 5 mirrored gray bags, 1 light maroon bag. """

def num_bags(amount,mybag):
    total = 0
    # print(f"Entering {mybag}")
    for bag in bags[mybag]:
        if "no other bag" in bag:
            return amount
        else:
            (num, verb, tbag, _) = bag.split()
            total += num_bags(int(num),f"{verb} {tbag}")
    print(f"{total} {mybag}")
    return amount + amount*total
        
print(num_bags(0,MYBAG))