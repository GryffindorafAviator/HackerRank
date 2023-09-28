#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the 'superDigit' function below.
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k

def superDigit(n, k):
    a = 0
    
    for i in n:
        a += int(i)
    
    a *= k
    a = list(str(a))
    
    while len(a) > 1:
        temp = 0
        
        for d in a:
            temp += int(d)
        
        a = list(str(temp))
    
    return a[0]    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()
