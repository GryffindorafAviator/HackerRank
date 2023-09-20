#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the 'timeConversion' function below.
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.

def timeConversion(s):
    ans = ""
    
    if s[-2] == 'A':
        if s[0] == '1' and s[1] == '2':
            ans = "00" + s[2:-2]
        else:
            ans = s[0:-2]
    else:
        if s[0] == '1' and s[1] == '2':
            ans = s[0:-2]
        else:
            temp = int(s[0:2])
            temp += 12
            temp = str(temp)
            ans = temp + s[2:-2]
    
    return ans
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
