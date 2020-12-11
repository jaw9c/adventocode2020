#!/usr/bin/python3
import sys
import itertools
import string
import math
import functools 

input = sys.argv[1]

def concat(listolists):
    return [item for sublist in listolists for item in sublist]

input_list = list(map(list, input.split("\n")))
print(len(input_list[0]))

def num_occ_adj(grid, x, y):
    count = 0
    for i in [-1,0,1]:
        if 0 <= x + i < len(grid):
            for j in [-1,0,1]:
                if 0 <= y + j < len(grid[0]):
                    if grid[x+i][y+j] == "#" and not (i == 0 and j == 0):
                        count += 1
    return count

def run_phase(grid):
    new_grid = [x.copy() for x in grid]
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "L" and num_occ_adj(grid, i, j) == 0:
                new_grid[i][j] = "#"
            elif grid[i][j] == "#" and num_occ_adj(grid, i, j) >= 4:
                new_grid[i][j] = "L"
    return new_grid

def pp(grid):
    print("\n".join(list(map("".join,step))))
    print("-------------")

done = False
while(not done):
    step = run_phase(input_list)
    pp(step)
    if concat(step) == concat(input_list):
        done=True
    else:
        input_list = step

print(sum([1 for x in concat(input_list) if x == "#"]))