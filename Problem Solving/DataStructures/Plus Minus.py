#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the 'plusMinus' function below.
# The function accepts INTEGER_ARRAY arr as parameter.

def plusMinus(arr):
    cnt_plus = 0
    cnt_minus = 0
    cnt_zero = 0
    
    for n in arr:
        if n > 0:
            cnt_plus += 1
        elif n < 0:
            cnt_minus += 1
        else:
            cnt_zero += 1
    
    total = cnt_zero + cnt_plus + cnt_minus
    
    rt_p = cnt_plus / total
    rt_m = cnt_minus / total
    rt_z = cnt_zero / total
    
    print(format(rt_p, '.6f'))
    print(format(rt_m, '.6f'))
    print(format(rt_z, '.6f'))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
