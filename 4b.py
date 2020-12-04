#!/usr/bin/python3
import sys
import itertools
import string

input = sys.argv[1]

def concat(listolists):
    return [item for sublist in listolists for item in sublist]

def clean(line):
    items = concat([x.split(" ") for x in line.split("\n")])
    return {key: value for [key, value] in map(lambda x: x.split(":"), items)}

input_list = list(map(clean, input.split("\n\n")))

def has_required(item):
    if len(item) is 8:
        return True
    if len(item) is 7:
        if item.get('cid') is None:
            return True

def valid_range(field, min, max):
    if len(field) is not 4 or int(field) < min or int(field) > max:
        return False
    return True

def valid_hgt(field):
    measure = field[-2:]
    if measure == "in":
        number = int(field[:-2])
        return 59 <= number <= 76
    if measure == "cm":
        number = int(field[:-2])
        return 150 <= number <= 193 
    return False

def valid_hcl(field):
    if field[0] != "#":
        return False
    if len(field[1:]) is not 6:
        return False
    return all(c in string.hexdigits for c in field[1:])

def valid_ecl(field):
    return field in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

def isValid(item):
    if not has_required(item):
        return False
    if not valid_range(item.get('byr'), 1920, 2020):
        return False
    if not valid_range(item.get('iyr'), 2010, 2020):
        return False
    if not valid_range(item.get('eyr'), 2020, 2030):
        return False
    if not valid_hgt(item.get('hgt')):
        return False
    if not valid_hcl(item.get('hcl')):
        return False
    if not valid_ecl(item.get('ecl')):
        return False
    if not len(item.get('pid')) is 9:
        return False
    return True
    
print(len(list(filter(isValid, input_list))))