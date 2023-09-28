#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the 'counterGame' function below.
# The function is expected to return a STRING.
# The function accepts LONG_INTEGER n as parameter.

def counterGame(n):
    cnt = 0
    power_two = powerTwo(n)
    
    while n > 1:
        if n in power_two:
            n /= 2
        else:
            for i in range(len(power_two) - 1, -1, -1):
                if power_two[i] < n:
                    n -= power_two[i]
                    
                    break
        
        cnt += 1
    
    return "Louise" if cnt % 2 == 1 else "Richard"

def powerTwo(n):
    ans = []
    temp = 1
    
    while temp <= n:
        ans.append(temp)
        temp *= 2
    
    return ans
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = counterGame(n)

        fptr.write(result + '\n')

    fptr.close()
