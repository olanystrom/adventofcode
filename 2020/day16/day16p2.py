#!/usr/bin/env python
import sys
# import numpy as np
sys.path.insert(1, sys.path[0] + '/..')  # Add parent of my directory to path
import AOC  ## pylint: disable=import-error
lines = AOC.loadInput(None,'day16.data')

""" Day 16: Ticket Translation """

def check_invalid(ticket):
    for num in ticket:
        valid = False
        for rule in rules:
            if valid:
                continue
            a,b,c,d = rules[rule]
            if ((a <= num <= b) or (c <= num <= d)):
                valid = True
                continue
        if not valid:
            return True
    return False

def matchrule(rule,row):
    a,b,c,d = rule
    for num in row:
        if ((a <= num <= b) or (c <= num <= d)):
            pass
        else:
            # print("invalid", a,b,c,d,num)
            return False
    return True

def matchrow(row):
    matched = list()   
    for rule in rules:
        a,b,c,d = rules[rule]
        # print(rule,a,b,c,d)
        valid = matchrule(rules[rule], row)
        if valid:
            matched.append(rule)
    return matched

def getsoloname(rownames):
    # print(rownames)
    for row in rownames:
        if len(rownames[row]) == 1:
            name = rownames[row]
            rownames.pop(row)
            return row, name[0], rownames

    # print("-" * 80)
    # for row in rownames:
    #     print(len(rownames[row]))
    # print(rownames)
    print("FAIL")
    return None

def deleterow(name, rownames):
    newnames = dict()
    for row in rownames:
        nn2 = list()
        for names in rownames[row]:
            # print(names)
            if names == name:
                pass
            else:
                nn2.append(names)
        newnames[row] = nn2
    # print(name, "new", newnames)
    return newnames

state=0
rules = dict()
ticket = list()
keeptickets = list(list())
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
        # print(line)
        ticket = [int(x) for x in line.split(',')]
    elif state == 2:
        if "ticket" in line:
            continue
        nt = [int(x) for x in line.split(',')]
        if not check_invalid(nt):
            keeptickets.append(nt)

# print(ticket)

# ktarray = np.array(keeptickets)
# rows = np.rot90(ktarray,axes=(1,0))
# transform to rows
rows = list()
tmp = list()
for a in range(len(keeptickets[0])):
    for b in keeptickets:
        tmp.append(b[a])
    rows.append(tmp)
    tmp = list()

rownames = dict()
# print("rowmaking")
for i,row in enumerate(rows):
    # print("row: ", i)
    mrow = matchrow(row)
    # print("mrow", i,mrow)
    rownames[i] = mrow

# print("*" * 80)
# print("0", rows[0])
# print("1", rows[1])
# print("2", rows[2])
# print("19", rows[19])
# print("*" * 80)

answer = 1
while True:
    row, name, rest = getsoloname(rownames)
    # print(row,name)
    if "departure" in name:
        print(f"row: {row}\tmyticket: {ticket[row]}\ttotal: {answer}\tname: {name}")
        answer *= ticket[row]
    rownames = rest
    rownames = deleterow(name, rownames)
    if len(rest) == 0:
        break


print(answer)
# print(rules)
# print(ticket)
# print(keeptickets)
# print(error)
AOC.printTimeTaken()    