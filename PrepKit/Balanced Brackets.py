#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the 'isBalanced' function below.
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.

def isBalanced(s):
    stack = []
    
    for c in s:
        if c in ['(', '[', '{']:
            stack.append(c)
        else:
            if stack == []:
                return "NO"
                
            match = stack.pop(-1)
            
            if c == ')' and match != '(':
                return "NO"
            
            if c == ']' and match != '[':
                return "NO"
            
            if c == '}' and match != '{':
                return "NO"
    
    if stack != []:
        return "NO"
               
    return "YES"            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
