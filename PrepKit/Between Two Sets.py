#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the 'getTotalX' function below.
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b

def getTotalX(a, b):
    lower = max(a)
    upper = min(b)
    
    cndtt = []
    
    for c in range(lower, upper + 1):
        if upper % c == 0:
            cndtt.append(c)
    
    cndtt1 = []
    
    for c1 in cndtt:
        is_cndtt = True
        
        for e1 in a:
            if c1 % e1 != 0:
                is_cndtt = False
                
                break
        
        if is_cndtt:
            cndtt1.append(c1)
            
    cndtt2 = []
    
    for c2 in cndtt1:
        is_cndtt1 = True
        
        for e2 in b:
            if e2 % c2 != 0:
                is_cndtt1 = False
                
                break
        
        if is_cndtt1:
            cndtt2.append(c2)
    
    return len(cndtt2)
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
