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

def test(input):
    accumulator = 0
    pointer = 0
    seen_lines = set()

    while(pointer not in seen_lines):
        if pointer == len(input):
            return accumulator
        (cmd, value) = input[pointer]
        seen_lines.add(pointer)
        if cmd == "nop":
            pointer += 1
        if cmd == "acc":
            accumulator += value
            pointer += 1
        if cmd == "jmp":
            pointer += value
    return None

for idx, instr in enumerate(input_list): 
    if instr[0] == "jmp":
        res = test(input_list[:idx] + [("nop", instr[1])] + input_list[idx+1:])
        print(res) if res else None
    if instr[0] == "nop":
        res = test(input_list[:idx] + [("jmp", instr[1])] + input_list[idx+1:])
        print(res) if res else None

