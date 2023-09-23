#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the 'pangrams' function below.
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.

def pangrams(s):
    l = [0] * 26
    
    for c in s:
        if c == " ":
            continue
        
        l[ord(c.lower()) - ord('a')] = 1
        
    for i in l:
        if i == 0:
            return "not pangram"
    
    return "pangram"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()
