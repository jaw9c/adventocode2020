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

    return (int(f"0b{row_bin}", 2), int(f"0b{col_bin}", 2))

my_ids = set([clean(x) for x in input_list])
all_ids = set(itertools.product(range(107)[2:], range(7)))

(row, col) = list(all_ids - my_ids)[0]

print(row * 8 + col)
