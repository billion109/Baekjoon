import sys
from collections import defaultdict, deque
input = sys.stdin.readline

N, M = map(int, input().split())
edge = defaultdict(list)
visited = [0 for i in range(N)]
stack = deque([])
ans = 0

for i in range(M):
    fr,to = map(int, input().split())
    edge[fr].append(to)
    edge[to].append(fr)

while sum(visited)<N:
    if len(stack)==0:
        stack.append(visited.index(0)+1)
        ans+=1

    while len(stack)>0:
        cur = stack.pop()
        visited[cur-1] = 1
        for i in edge[cur]:
            if visited[i-1]==0:
                stack.append(i)
print(ans)