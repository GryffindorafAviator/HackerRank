#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the 'birthday' function below.
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY s
#  2. INTEGER d
#  3. INTEGER m

def birthday(s, d, m):
    n = len(s)
    cnt = 0
    
    if n < m:
        return cnt
    
    sliding = sum(s[:m])
    
    if sliding == d:
        cnt += 1
    
    front = 0
    rear = m
    
    while rear < n:
        sliding = sliding - s[front] + s[rear]
        
        if sliding == d:
            cnt += 1
        
        front += 1
        rear += 1
    
    return cnt
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    first_multiple_input = input().rstrip().split()

    d = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()
