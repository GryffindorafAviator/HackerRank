#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the 'gridChallenge' function below.
# The function is expected to return a STRING.
# The function accepts STRING_ARRAY grid as parameter.

def gridChallenge(grid):
    s_len = 0
    
    for i in range(len(grid)):
        l = list(grid[i])
        s_len = len(l)
        l.sort()
        grid[i] = l
    
    for k in range(s_len):
        for j in range(len(grid) - 1):
            if grid[j][k] > grid[j + 1][k]:
                return "NO"
    
    return "YES"
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        grid = []

        for _ in range(n):
            grid_item = input()
            grid.append(grid_item)

        result = gridChallenge(grid)

        fptr.write(result + '\n')

    fptr.close()
