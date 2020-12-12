#!/usr/bin/python3
import sys
import itertools
import string
import math
import functools 

input = sys.argv[1]

def clean(line):
    return (line[0], int(line[1:]))

input_list = list(map(clean, input.split("\n")))

def move(pos, instr):
    (action, mag) = instr
    if action == "N":
        return (pos[0], pos[1] + mag, pos[2])
    if action == "E":
        return (pos[0] + mag, pos[1], pos[2])
    if action == "S":
        return (pos[0], pos[1] - mag, pos[2])
    if action == "W":
        return (pos[0] - mag, pos[1], pos[2])
    if action == "L":
        return  (pos[0], pos[1], (pos[2] - mag) % 360)
    if action == "R":
        return  (pos[0],pos[1], (pos[2] + mag) % 360)
    if action == "F":
        return (pos[0] + mag* math.sin(math.radians(pos[2])), pos[1] +mag * math.cos(math.radians(pos[2])), pos[2])

pos = (0, 0, 90)
for instr in input_list:
    pos = move(pos, instr)

print(sum(map(abs, pos[0:2])))