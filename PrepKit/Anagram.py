#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the 'anagram' function below.
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.

def anagram(s):
    n = len(s)
    
    if n % 2 != 0:
        return -1
    
    cnt = {}
    
    for i in range(n // 2):
        cnt[s[i]] = cnt.get(s[i], 0) + 1
    
    same = 0
    
    for j in range(n // 2, n):
        if s[j] in cnt and cnt[s[j]] > 0:
            cnt[s[j]] -= 1
            same += 1
            
    return n // 2 - same

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = anagram(s)

        fptr.write(str(result) + '\n')

    fptr.close()
