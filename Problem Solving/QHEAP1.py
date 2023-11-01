import heapq

pq = []
pq_del = []
q = int(input())

while q > 0:
    op = list(map(int, input().split()))
    
    if op[0] == 1:
        heapq.heappush(pq, op[1])
    elif op[0] == 2:
        heapq.heappush(pq_del, op[1])
    else:
        while pq_del != [] and pq_del[0] == pq[0]:
            heapq.heappop(pq)
            heapq.heappop(pq_del)
            
        print(pq[0])
    
    q -= 1
