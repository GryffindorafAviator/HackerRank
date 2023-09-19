import heapq

n = int(input())
min_heap = []
deleted_set = set()

for _ in range(n):
    command = list(map(int, input().split(' ')))
    
    if command[0] == 1:
        if command[1] in deleted_set:
            deleted_set.remove(command[1])
            
            continue
        
        heapq.heappush(min_heap, command[1])
    elif command[0] == 2:
        deleted_set.add(command[1])
    else:
        while min_heap[0] in deleted_set:
            deleted_set.remove(min_heap[0])
            heapq.heappop(min_heap)
               
        print(min_heap[0])
