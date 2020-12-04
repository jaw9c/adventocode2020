#!/usr/bin/python3
import sys
import itertools

input = sys.argv[1]

def concat(listolists):
    return [item for sublist in listolists for item in sublist]

def clean(line):
    items = concat([x.split(" ") for x in line.split("\n")])
    return {key: value for [key, value] in map(lambda x: x.split(":"), items)}

input_list = list(map(clean, input.split("\n\n")))

def isValid(item):
    if len(item) is 8:
        return True
    if len(item) is 7:
        if item.get('cid') is None:
            return True

print(len(list(filter(isValid, input_list))))