#!/bin/python3

import math
import os
import random
import re
import sys

def truckTour(petrolpumps):
    total = 0
    cur = 0
    start = 0
    n = len(petrolpumps)
        
    for i in range(n):
        petrol, distance = petrolpumps[i]
        total += (petrol - distance)
        cur += (petrol - distance)
        
        if cur < 0:
            cur = 0
            start = i + 1
    
    return start if total >= 0 else -1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    petrolpumps = []

    for _ in range(n):
        petrolpumps.append(list(map(int, input().rstrip().split())))

    result = truckTour(petrolpumps)

    fptr.write(str(result) + '\n')

    fptr.close()
