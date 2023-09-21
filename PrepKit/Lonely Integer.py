#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the 'lonelyinteger' function below.
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.

def lonelyinteger(a):
    a.sort()
    n = len(a)
    
    if n == 1:
        return a[0]
    
    slow = 0
    fast = 1
    
    while fast < n:
        if a[slow] == a[fast]:
            slow += 2
            fast += 2
        else:
            return a[slow]
    
    return a[n - 1]
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)

    fptr.write(str(result) + '\n')

    fptr.close()
