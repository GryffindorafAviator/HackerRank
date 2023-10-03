#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the 'isValid' function below.
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.

def isValid(s):
    if len(s) == 1:
        return "YES"
        
    cnt = {}
    
    for c in s:
        cnt[c] = cnt.get(c, 0) + 1
        
    cnt_val = list(cnt.values())
    cnt_val.sort()
    
    min_cnt = cnt_val[0]
    min_2nd = cnt_val[1]
    max_cnt = cnt_val[-1]
    max_2nd = cnt_val[-2]
    
    if min_cnt == max_cnt:
        return "YES"
    
    if min_cnt + 1 == max_cnt and min_2nd == max_cnt:
        return "YES"
        
    if min_cnt == max_cnt - 1 and min_cnt == max_2nd:
        return "YES"
    
    if min_cnt == 1 and min_2nd == max_cnt:
        return "YES"
        
    return "NO"
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
