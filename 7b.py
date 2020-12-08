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

def do_bago(bagz, count):
    if len(bagz) == 0:
        return count
    more_bag = tree[bagz[0]]
    if more_bag.get('other bags.') is not None:
        return 1
    count = 1
    for bag in more_bag:
        count += int(more_bag[bag]) * do_bago([bag], count)
    return count


print(do_bago(["shiny gold"], 0) -1)