#!/usr/bin/python3
import sys
import itertools
import string
import math
import functools 

input = sys.argv[1]

def clean(line):
    return int(line) if line != "x" else None

buses = list(map(clean, input.split("\n")[1].split(",")))

curr = 0
jump = 1
for idx, bus in enumerate(buses):
    if bus is None:
        continue

    while (curr + idx) % bus != 0:
        curr = curr + jump

    jump = jump * bus

print(curr, jump)



