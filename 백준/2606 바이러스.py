import sys
from collections import deque, defaultdict
input = sys.stdin.readline

n = int(input())
m = int(input())
dic = defaultdict(list)
visited = set()
q = deque([1])
for i in range(m):
    fr, to = map(int,input().split())
    dic[fr].append(to)
    dic[to].append(fr)

while len(q)>0:
    curr = q.pop()
    visited.add(curr)
    for i in dic[curr]:
        if i not in visited:
            q.append(i)
print(len(visited)-1)