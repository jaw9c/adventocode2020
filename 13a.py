#!/usr/bin/python3
import sys
import itertools
import string
import math
import functools 

input = sys.argv[1]

leaving_time = int(input.split("\n")[0])
buses = list(map(int, [x for x in input.split("\n")[1].split(",") if x is not "x"]))

def mino(x, y):
    return x if x[1] < y[1] else y

bus, time = functools.reduce(mino, [(bus, math.ceil(leaving_time/bus) * bus) for bus in buses])

print(bus * (time - leaving_time))