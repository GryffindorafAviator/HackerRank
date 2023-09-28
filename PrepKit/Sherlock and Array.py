#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the 'balancedSums' function below.
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY arr as parameter.

def balancedSums(arr):
    total = sum(arr)
    front_sum = 0
    
    for i in range(len(arr)):
        if front_sum == (total - arr[i]) / 2:
            return "YES"
        
        front_sum += arr[i]
    
    return "NO"
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input().strip())

    for T_itr in range(T):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = balancedSums(arr)

        fptr.write(result + '\n')

    fptr.close()
