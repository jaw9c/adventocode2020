#!/usr/bin/python3
import sys
import itertools
import string
import math
import functools 

input = sys.argv[1]

def concat(listolists):
    return [item for sublist in listolists for item in sublist]

input_list = list(input.split("\n\n"))

count = 0
for item in input_list:
    all_ppz = item.split('\n')
    initial = set(all_ppz[0])
    for p in all_ppz:
        initial = set(p).intersection(initial)
    count += len(initial)

print(count)