#!/usr/bin/python3
import sys

def clean(line):
    return line

input_list = list(map(clean, sys.argv[1].split("\n")))

count = 0
for idx, y in enumerate(input_list):
    if y[(idx * 3) % len(y)] == "#":
        count += 1

print(count)
