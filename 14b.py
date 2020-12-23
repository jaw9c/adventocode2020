#!/usr/bin/python3
import sys
import itertools
import string
import math
import functools 

input = sys.argv[1]

def clean(line):
    cmd, value = line.split(" = ")
    if cmd == "mask":
        return ("M", value)
    else:
        return ("A", int(cmd.split("[")[1][:-1]), int(value))

input_list = list(map(clean, input.split("\n")))

def doMask(maskStr, value):
    asBin = list(map(int, bin(value)[2:]))
    pad = [0 for x in range(36 - len(asBin))] + asBin
    masked = list(map(str, [pad[i] if maskStr[i] == "0" else "0" if maskStr[i] == "Z" else "1" for i in range(36)]))
    return int("".join(masked), 2)


def doWrite(reg, address, mask, value):
    for idx, bit in enumerate(mask):
        if bit == "X":
            doWrite(reg, address, mask[:idx] + "1" + mask[idx+1:], value)
            doWrite(reg, address, mask[:idx] + "Z" + mask[idx+1:], value)
            return
    reg[doMask(mask, address)] = value

mask = None
reg = {}
for instr in input_list:
    cmd = instr[0]
    if cmd == "A":
        doWrite(reg, instr[1], mask, instr[2])
    elif cmd == "M":
        mask = instr[1]

print(sum([reg[k] for k in reg]))