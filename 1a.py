#!/usr/bin/python3
import sys
import itertools

input_list = list(map(int, sys.argv[1].split("\n")))

def bun_da_ting():
    for (x, y) in itertools.product(input_list, input_list):
        if x + y == 2020:
            yield x * y

print(next(bun_da_ting()))