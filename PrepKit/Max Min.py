#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the 'maxMin' function below.
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr

def maxMin(k, arr):
    arr.sort()
    glb_min = sys.maxsize
    
    st = 0
    ed = k - 1
    
    while ed < len(arr):
        glb_min = min(glb_min, abs(arr[ed] - arr[st]))
        st += 1
        ed += 1
        
    return glb_min  

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    k = int(input().strip())

    arr = []

    for _ in range(n):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = maxMin(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
