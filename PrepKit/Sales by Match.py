#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the 'sockMerchant' function below.
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar

def sockMerchant(n, ar):
    ar.sort()
    
    cnt = 1
    pairs = 0
    
    for i in range(1, n):
        if ar[i] == ar[i - 1]:
            cnt += 1
        else:
            pairs += cnt // 2
            cnt = 1
    
    pairs += cnt // 2
    
    return pairs 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
