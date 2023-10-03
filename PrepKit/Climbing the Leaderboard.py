#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the 'climbingLeaderboard' function below.
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player

def climbingLeaderboard(ranked, player):
    n = len(ranked)
    rank = 1
    ranking = {}
    ranking[ranked[0]] = 1
    
    for i in range(1, n):  
        if ranked[i] < ranked[i - 1]:
            rank += 1
            
        ranking[ranked[i]] = rank
    
    result = []
    last = ranking[ranked[-1]]
    
    for score in player:
        if score >= ranked[0]:
            result.append(1)
            
            continue
            
        if score == ranked[-1]:
            result.append(last)
            
            continue
        
        if score < ranked[-1]:
            result.append(last + 1)
            
            continue
        
        left = 0
        right = n - 1
        
        while left < right:
            mid = left + (right - left) // 2
            
            if score == ranked[mid]:
                result.append(ranking[ranked[mid]])
                
                break
            elif score < ranked[mid]:
                left = mid
                
                if right - left == 1:
                    result.append(ranking[ranked[left]] + 1)
                    
                    break
            else:
                right = mid
                
                if right - left == 1:
                    result.append(ranking[ranked[left]] + 1)
                    
                    break
    
    return result            
                    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
