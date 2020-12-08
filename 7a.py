#!/usr/bin/python3
import sys
import itertools
import string
import math
import functools 

input = sys.argv[1]

def concat(listolists):
    return [item for sublist in listolists for item in sublist]

input_list = list(input.split("\n"))

tree = {}

for rule in input_list:
    sp = rule.split(' bags contain ')
    tree[sp[0]] = {}
    for lower in sp[1].split(', '):
        pp = lower.split(" ")
        num_sub_bag = pp[0]
        name_sub_bag = " ".join(pp[1:3])
        
        tree[sp[0]][name_sub_bag] = num_sub_bag


containers = ["shiny gold"]
for x in range(len(tree)):
    new_contain = set(containers)
    for k in tree:
        for c in containers:
            if tree[k].get(c) is not None:
                new_contain.add(k)
    containers = list(new_contain)

print(len(containers) - 1)
        