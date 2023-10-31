#!/bin/python3

import math
import os
import random
import re
import sys

def maxSubarray(arr):
    ans_arr = -sys.maxsize - 1
    ans_seq = -sys.maxsize - 1
    cur_acc = 0
    
    for num in arr:
        ans_seq = max(ans_seq + num, num, ans_seq)
        
        cur_acc += num
        ans_arr = max(ans_arr, cur_acc)
            
        if cur_acc < 0:
            cur_acc = 0
        
    return [ans_arr, ans_seq]    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = maxSubarray(arr)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
