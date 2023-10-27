#!/bin/python3

import math
import os
import random
import re
import sys

def equalStacks(h1, h2, h3):
    height1 = sum(h1)
    height2 = sum(h2)
    height3 = sum(h3)
    height = min(height1, height2, height3)
    i1 = 0
    i2 = 0
    i3 = 0
    
    while (height1 != height or height2 != height or height3 != height):
        if height1 > height and i1 < len(h1):
            height1 -= h1[i1]
            i1 += 1
        
        if height2 > height and i2 < len(h2):
            height2 -= h2[i2]
            i2 += 1
        
        if height3 > height and i3 < len(h3):
            height3 -= h3[i3]
            i3 += 1
        
        if i1 == len(h1) or i2 == len(h2) or i3 == len(h3):
            return 0
            
        height = min(height1, height2, height3)
    
    return height

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n1 = int(first_multiple_input[0])

    n2 = int(first_multiple_input[1])

    n3 = int(first_multiple_input[2])

    h1 = list(map(int, input().rstrip().split()))

    h2 = list(map(int, input().rstrip().split()))

    h3 = list(map(int, input().rstrip().split()))

    result = equalStacks(h1, h2, h3)

    fptr.write(str(result) + '\n')

    fptr.close()
