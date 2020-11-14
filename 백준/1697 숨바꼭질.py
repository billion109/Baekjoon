import sys
input = sys.stdin.readline
from collections import deque
N, K = map(int, input().split())
q = deque([])
q.append([N,0])
visited = set()

def bfs():
    if K<=N:
        print(N-K)
        return
    while len(q)>0:
        t = q.popleft()
        pos,time = t[0],t[1]
        visited.add(pos)
        if pos == K:
            print(time)
            return

        if pos>0 and (pos-1)not in visited:
            q.append([pos-1,time+1])

        if pos<100000 and (pos+1) not in visited:
            q.append([pos+1,time+1])

        if pos*2<=100000 and (pos*2) not in visited:
            q.append([pos*2,time+1])

bfs()
