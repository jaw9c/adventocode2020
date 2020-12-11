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

def num_occ_adj(grid, x, y):
    count = 0
    for i in [-1,0,1]:
        if 0 <= x + i < len(grid):
            for j in [-1,0,1]:
                if 0 <= y + j < len(grid[0]):
                    done=False
                    z=1
                    while(not done and -1 < x+(z*i) < len(grid) and  -1 < y+(z*j) < len(grid[0])):
                        if j == 0 and i == 0:
                            done=True
                        elif grid[x+(z*i)][y+(z*j)] == "#":
                            done=True
                            count += 1
                        elif grid[x+(z*i)][y+(z*j)] == "L":
                            done=True
                        z += 1
    return count

def run_phase(grid):
    new_grid = [x.copy() for x in grid]
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "L" and num_occ_adj(grid, i, j) == 0:
                new_grid[i][j] = "#"
            elif grid[i][j] == "#" and num_occ_adj(grid, i, j) >= 5:
                new_grid[i][j] = "L"
    return new_grid

def pp(grid):
    print("\n".join(list(map("".join,step))))
    print("-------------")

done = False
while(not done):
    print(num_occ_adj(input_list, 1, 0))
    step = run_phase(input_list)
    pp(step)
    if concat(step) == concat(input_list):
        done=True
    else:
        input_list = step

print(sum([1 for x in concat(input_list) if x == "#"]))