#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the 'caesarCipher' function below.
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k

def caesarCipher(s, k):
    ans = ""
    k %= 26
    
    for c in s:
        if c.isalpha():
            temp = ord(c) + k
            
            if c.islower():
                if temp - ord('a') > 25:
                    temp -= 26
            else:
                if temp - ord('A') > 25:
                    temp -= 26
                
            ans += chr(temp)
        else:
            ans += c
    
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
