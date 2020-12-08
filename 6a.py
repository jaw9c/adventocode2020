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

print(sum([len(set(concat(row.split('\n')))) for row in input_list]))