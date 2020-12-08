#!/usr/bin/python3
import sys
import itertools
import string
import math
import functools 

input = sys.argv[1]

input_list = list(input.split("\n"))

def clean(row):
    row_bin = "".join(list(map(lambda x: "1" if x is "B" else "0", row[:7])))
    col_bin = "".join(list(map(lambda x: "1" if x is "R" else "0", row[7:])))

    return 8 * int(f"0b{row_bin}", 2) + int(f"0b{col_bin}", 2)

print(functools.reduce(lambda a,b : a if a > b else b, map(clean, input_list)))
