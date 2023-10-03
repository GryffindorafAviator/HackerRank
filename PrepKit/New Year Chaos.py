#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the 'minimumBribes' function below.
# The function accepts INTEGER_ARRAY q as parameter.

def minimumBribes(q):
    n = len(q)
    
    for i in range(n):
        if q[i] - (i + 1) > 2:
            print("Too chaotic")
            
            return
    
    total = 0
    
    for j in range(n):
        cnt = 0
        
        for k in range(0, n - 1 - j):
            if q[k] > q[k + 1]:
                q[k], q[k + 1] = q[k + 1], q[k]
                cnt += 1

        total += cnt
    
    print(total)

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
