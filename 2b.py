#!/usr/bin/python3
import sys

def clean(line):
    [range, letter, password] = line.split(" ")
    [p1, p2] = range.split("-")

    return (int(p1) -1 , int(p2) - 1, letter[0], password)

input_list = list(map(clean, sys.argv[1].split("\n")))

def is_valid(line):
    (p1, p2, letter, password) = line
    return (password[p1] is letter) ^ (password[p2] is letter)

num_passwords = sum(1 for line in input_list if is_valid(line))

print(num_passwords)