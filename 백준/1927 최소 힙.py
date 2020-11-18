import sys
input = sys.stdin.readline
import heapq

q =[]
N = int(input())
for i in range(N):
    temp = int(input())
    if temp==0:
        if len(q)>0:
            print(heapq.heappop(q))
        else:
            print(0)
    else:
        heapq.heappush(q,temp)