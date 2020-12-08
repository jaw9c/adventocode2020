#!/usr/bin/python3
import sys

def clean(line):
    return line

input_list = list(map(clean, sys.argv[1].split("\n")))

def no_trees(slope_x, slope_y):
    count = 0
    for idx in range(int(len(input_list) / slope_y)):
        if input_list[slope_y*idx][(idx * slope_x) % len(input_list[0])] == "#":
            print(idx)
            count += 1
    return count

mul = 1
for slope in [(1,1), (3,1), (5,1), (7,1), (1,2)]:
    mul *= no_trees(*slope)

print(mul)