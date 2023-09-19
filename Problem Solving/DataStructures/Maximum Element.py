#!/bin/python3

import math
import os
import random
import re
import sys
import heapq

# Complete the 'getMax' function below.
# The function is expected to return an INTEGER_ARRAY.
# The function accepts STRING_ARRAY operations as parameter.

def getMax(operations):
    stack = []
    ans = []
    max_heap = []
    
    for op in operations:
        op = list(map(int, op.split(' ')))
        
        if op[0] == 1:
            stack.append(op[1])
            heapq.heappush(max_heap, -op[1])
        elif op[0] == 2:
            temp = stack.pop(-1)
            max_heap.remove(-temp)
            heapq.heapify(max_heap)
        else:
            ans.append(-max_heap[0])
    
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ops = []

    for _ in range(n):
        ops_item = input()
        ops.append(ops_item)

    res = getMax(ops)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
