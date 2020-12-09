#!/usr/bin/python3
import sys
import itertools
import string
import math
import functools 

input = sys.argv[1]

input_list = list(map(int, input.split("\n")))

WINDOW_SIZE = 25

for idx, num in enumerate(input_list[WINDOW_SIZE:]):
    window = input_list[idx:idx+ WINDOW_SIZE]
    all_sums = [x+y for (x,y) in itertools.combinations(window, r=2)]
    if(num not in all_sums):
        print(num)
