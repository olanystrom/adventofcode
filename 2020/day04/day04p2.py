#!/usr/bin/env python
import os
import sys
with open(os.path.join(sys.path[0],'day04.data')) as fp:
   lines = [x.strip() for x in fp.readlines()]

reqfields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

def validbyr(data):
    """  byr (Birth Year) - four digits; at least 1920 and at most 2002. """
    if 1920 <= data <= 2002:
        return 1
    return 0

def validiyr(data):
    """ iyr (Issue Year) - four digits; at least 2010 and at most 2020. """
    if 2010 <= data <= 2020:
        return 1
    return 0

def valideyr(data):
    """ eyr (Expiration Year) - four digits; at least 2020 and at most 2030. """
    if 2012 <= data <= 2030:
        return 1
    return 0

def validhgt(data):
    """
    hgt (Height) - a number followed by either cm or in:
        If cm, the number must be at least 150 and at most 193.
        If in, the number must be at least 59 and at most 76.
    """
    if ("in" in data):
        if(data.rstrip('in').isdigit()):
            if 59 <= int(data.rstrip('in')) <= 76:
                return  1
    if ("cm" in data):
        if(data.rstrip('cm').isdigit()):
            if 150 <= int(data.rstrip('cm')) <= 193:
                return  1
    return 0

def _ishex(data):
    try:
        int(data, 16)
        return True
    except ValueError:
        return False

def validhcl(data):
    """ hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f. """
    if len(data) == 7:
        if _ishex(data.lstrip("#")):
            return 1
    return 0

def validecl(data):
    """ ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth. """
    return (data in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"])

def validpid(data):
    """ pid (Passport ID) - a nine-digit number, including leading zeroes. """
    return len(data) == 9

def isvalidpassport(indict):
    count = 0
    for f in indict.keys():
        if f in reqfields:
            if f == "byr":
                count += validbyr(int(indict[f]))
            elif f == "iyr":
                count += validiyr(int(indict[f]))
            elif f == "eyr":
                count += valideyr(int(indict[f]))
            elif f == "hgt":
                count += validhgt(indict[f])
            elif f == "hcl":
                count += validhcl(indict[f])
            elif f == "ecl":
                count += validecl(indict[f])
            elif f == "pid":
                count += validpid(indict[f])
    if count == 7:
        return True
    return False

new = 0
check = dict()
totalvalid = 0
for line in lines:
    if line == "":
        new = 1
        if isvalidpassport(check):
            totalvalid += 1
        check = dict()
    else:
        new = 0
        fields = line.split()
        for field in fields:
            (f,d) = field.split(':')
            check[f] = d
if isvalidpassport(check):
    totalvalid += 1

print(totalvalid)