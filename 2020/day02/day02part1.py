#!/usr/bin/env python
with open('day02.data') as fp:
   lines = [x.strip() for x in fp.readlines()]

def validpass(line):
    # format 8-9 x: xxxxxxxrk
    (code, password) = line.split(':')
    (num, tecken) = code.split(' ')
    (first,second) = num.split('-')
    (low,high) = [int(x) for x in num.split('-')]
    teckencount = len([x for x in password if tecken in x])
    if int(low) <= (teckencount) <= int(high):
            return True
    return False

validcount = 0
for line in lines:
    if validpass(line):
        validcount += 1
print(f"Total valid: {validcount}")