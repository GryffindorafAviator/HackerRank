#!/bin/python3

import math
import os
import random
import re
import sys
    
def prime(n, q):
    result = [2, 3]
    
    if q == 1:
        return [2]
        
    if q == 2:
        return result
    
    for i in range(4, n):
        find = True
        
        for j in result:
            if i % j == 0:
                find = False
                
                break
        
        if find:
            result.append(i)
            
        if len(result) == q:
            break
    
    return result
    
def waiter(number, q):
    prime_arr = prime(1000000, q)
    ans = []
    a = []
    b = []
    
    cnt = 0
    
    while cnt < q:
        p = prime_arr[cnt]
        
        if cnt > 0:
            number = a
            a = []
            b = []
        
        for n in number[::-1]:
            if n % p == 0:
                b.append(n)
            else:
                a.append(n)
        
        ans += b[::-1]
        
        if len(a) == 0:
            break
            
        cnt += 1
        
    ans += a[::-1]
    
    return ans                  

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    number = list(map(int, input().rstrip().split()))

    result = waiter(number, q)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
