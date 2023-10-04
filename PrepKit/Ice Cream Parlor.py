#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the 'icecreamParlor' function below.

# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
# 1. INTEGER m
# 2. INTEGER_ARRAY arr

def icecreamParlor(m, arr):
    complement = {}
    ans = []
    
    for i in range(len(arr)):
        if arr[i] in complement:
            ans.append(complement[arr[i]] + 1)
            ans.append(i + 1)
            
            break
        else:
            complement[m - arr[i]] = i
    
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        m = int(input().strip())

        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = icecreamParlor(m, arr)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
