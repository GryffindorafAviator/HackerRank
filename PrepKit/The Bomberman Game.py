#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the 'bomberMan' function below.
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING_ARRAY grid

def bomberMan(n, grid):
    if n == 1:
        return grid
        
    ROWS = len(grid)
    COLS = len(grid[0])
    sec_3 = [['O'] * COLS for _ in range(ROWS)]
    
    if n % 2 == 0:
        ans1 = [''.join(row1) for row1 in sec_3]
        
        return ans1
        
    DIRS = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    
    for r1 in range(ROWS):
        for c1 in range(COLS):
            if grid[r1][c1] == 'O':
                sec_3[r1][c1] = '.'
                
                for d1 in DIRS:
                    if 0 <= r1 + d1[0] and r1 + d1[0] < ROWS and 0 <= c1 + d1[1] and c1 + d1[1] < COLS:
                        sec_3[r1 + d1[0]][c1 + d1[1]] = '.'
    
    if n % 4 == 3:
        ans2 = [''.join(row2) for row2 in sec_3]
        
        return ans2
        
    sec_5 = [['O'] * COLS for _ in range(ROWS)]
    
    for r2 in range(ROWS):
        for c2 in range(COLS):
            if sec_3[r2][c2] == 'O':
                sec_5[r2][c2] = '.'
            
                for d2 in DIRS:
                    if 0 <= r2 + d2[0] and r2 + d2[0] < ROWS and 0 <= c2 + d2[1] and c2 + d2[1] < COLS:
                        sec_5[r2 + d2[0]][c2 + d2[1]] = '.'
    
    ans3 = [''.join(row3) for row3 in sec_5]
    
    return ans3

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    r = int(first_multiple_input[0])

    c = int(first_multiple_input[1])

    n = int(first_multiple_input[2])

    grid = []

    for _ in range(r):
        grid_item = input()
        grid.append(grid_item)

    result = bomberMan(n, grid)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
