#!/usr/bin/env python
import itertools
import re
import sys
sys.path.insert(1, sys.path[0] + '/..')  # Add parent of my directory to path
import AOC  ## pylint: disable=import-error
lines = AOC.loadInput(None,'day18.data')

""" Day 18: Operation Order """

"""
Now, addition and multiplication have different precedence levels, but they're not the ones you're familiar with.
Instead, addition is evaluated before multiplication.
"""

class Fucked():
    def __init__(self,number):
        self.number = number

    def __add__(self, other):
        if type(other) is not Fucked:
            # print(f"add {self.number} with {other}")
            return Fucked(self.number * other)
        # print(f"add {self.number} with {other.number}")
        return Fucked(self.number * other.number)

    def __radd__(self, other):
        if type(other) is not Fucked:
            # print(f"radd {self.number} with {other}")
            return Fucked(self.number + other)
        # print(f"radd {self.number} with {other.number}")
        return Fucked(self.number * other.number)

    def __mul__(self, other):
        if type(other) is not Fucked:
            # print(f"mul {self.number} with {other}")
            return (self.number + other)
        # print(f"mul {self.number} with {other.number}")
        return Fucked(self.number + other.number)

    def __rmul__(self, other):
        if type(other) is not Fucked:
            # print(f"rmul {self.number} with {other}")
            return Fucked(self.number * other)
        # print(f"rmul {self.number} with {other.number}")
        return Fucked(self.number + other.number)

    def __repr__(self):
        return f"Fucked({self.number})"

    def __int__(self):
        return int(self.number)

class AoCMath():
    def __init__(self, mymath):
        mymath = mymath.replace(" ", "")
        print(f"{mymath=}")
        while len(list(self.parenthetic_contents(mymath))) > 0:
            level, mmath = list(self.parenthetic_contents(mymath))[0]
            replace1 = f"({mmath})"
            # print(f"{level=} {mmath=}")
            # print(f"{replace1=} {self.evalmath(mmath)=}")
            mymath = mymath.replace(replace1,str(self.evalmath(mmath)))
            # print(f"{mymath=}")
        self.summa = int(self.evalmath(mymath))


    def evalmath(self, mathline):
        """ Evalutes every operation in a Fucked order
            replace * with  + and + with * and change what they do """
        # print(f"{mathline=}")
        mathline = mathline.replace('+', '_')
        mathline = mathline.replace('*', '+')
        mathline = mathline.replace('_', '* ')
        # print(f"{mathline=}")
        parts = re.split('(\W+)',mathline)
        first = Fucked(parts[0])
        delsumma = f"{first}"
        for part in parts[1:]:
            if part.isdigit():
                num = Fucked(part)
                delsumma += f"{last}{num}"
            else:
                last = part
        # print(f"{delsumma=} {eval(delsumma)=}")
        return int(eval(delsumma))


    """ https://stackoverflow.com/questions/4284991/parsing-nested-parentheses-in-python-grab-content-by-level """
    def parenthetic_contents(self,string):
        """Generate parenthesized contents in string as pairs (level, contents)."""
        stack = []
        for i, c in enumerate(string):
            if c == '(':
                stack.append(i)
            elif c == ')' and stack:
                start = stack.pop()
                yield (len(stack), string[start + 1: i])


def aocmath(line):
    aocm = AoCMath(line)
    return aocm.summa

# print(aocmath(lines[1]))
totsum = 0
for line in lines:
    print(aocmath(line))
    totsum += aocmath(line)

print(totsum)
AOC.printTimeTaken()