#!/usr/bin/python3
import sys

def clean(line):
    [range, letter, password] = line.split(" ")
    [min, max] = range.split("-")

    return (int(min), int(max), letter[0], password)

input_list = list(map(clean, sys.argv[1].split("\n")))

def is_valid(line):
    (min, max, letter, password) = line
    return password.count(letter) >= min and password.count(letter) <= max

num_passwords = sum(1 for line in input_list if is_valid(line))

print(num_passwords)
