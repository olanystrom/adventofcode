#!/usr/bin/env python
import sys
sys.path.insert(1, sys.path[0] + '/..')  # Add parent of my directory to path
import AOC  ## pylint: disable=import-error
lines = AOC.loadInput(None,'day16.data')

""" Day 16: Ticket Translation """

def check_invalid(ticket):
    for num in ticket:
        valid = False
        for rule in rules:
            a,b,c,d = rules[rule]
            if ((a <= num <= b) or (c <= num <= d)):
                valid = True
                continue
        if not valid:
            return num
    return 0

state=0
rules = dict()
ticket = list()
ntickets = list(list())
error = 0
for line in lines:
    if line == "" and state == 0:
        # print("state 1")
        state = 1
        continue
    elif line == "" and state == 1:
        # print("state 2")
        state = 2
        continue
    if state == 0:
        name, linerule = line.split(':')
        r1, r2 = linerule.split('or')
        r11,r12 = [int(x) for x in r1.split('-')]
        r21,r22 = [int(x) for x in r2.split('-')]
        rules[name] = (r11,r12,r21,r22)
    elif state == 1:
        if "ticket" in line:
            continue
        print(line)
        ticket = [int(x) for x in line.split(',')]
    elif state == 2:
        if "ticket" in line:
            continue
        nt = [int(x) for x in line.split(',')]
        ntickets.append(nt)
        error += check_invalid(nt)
   


# print(rules)
# print(ticket)
# print(ntickets)
print(error)
AOC.printTimeTaken()    