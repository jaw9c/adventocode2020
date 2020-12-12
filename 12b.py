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
    action, mag = instr
    ship_pos, waypoint = pos
    
    if action == "N":
        return (ship_pos, (waypoint[0], waypoint[1]  + mag))
    if action == "E":
        return (ship_pos, (waypoint[0] + mag, waypoint[1]))
    if action == "S":
        return (ship_pos, (waypoint[0], waypoint[1]  - mag))
    if action == "W":
        return (ship_pos, (waypoint[0] - mag, waypoint[1]))
    if action == "L":
        deg_mag = math.radians(mag)
        x =  math.cos(deg_mag) * waypoint[0] - math.sin(deg_mag) * waypoint[1]
        y = math.sin(deg_mag) * waypoint[0] + math.cos(deg_mag) * waypoint[1]
        return  (ship_pos, (x, y))
    if action == "R":
        deg_mag = math.radians(-mag)
        x = math.cos(deg_mag) * waypoint[0] - math.sin(deg_mag) * waypoint[1]
        y = math.sin(deg_mag) * waypoint[0] + math.cos(deg_mag) * waypoint[1]
        return  (ship_pos, (x, y))
    if action == "F":
        return ((ship_pos[0] + mag*waypoint[0], ship_pos[1] + mag*waypoint[1]), waypoint)

pos = ((0, 0), (10, 1))
for instr in input_list:
    pos = move(pos, instr)

print(sum(map(abs, pos[0][0:2])))