#!/usr/bin/python3
import sys
import itertools
import string
import math
import functools 

input = sys.argv[1]

def clean(line):
    return (line.split(" ")[0], int(line.split(" ")[1]))

input_list = list(map(clean, input.split("\n")))

accumulator = 0
pointer = 0
seen_lines = set()

while(pointer not in seen_lines):
    (cmd, value) = input_list[pointer]
    seen_lines.add(pointer)
    if cmd == "nop":
        pointer += 1
    if cmd == "acc":
        accumulator += value
        pointer += 1
    if cmd == "jmp":
        pointer += value

print(accumulator)