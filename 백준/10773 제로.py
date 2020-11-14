from collections import deque

q = deque([])
n = int(input())
for i in range(n):
    t = int(input())
    if t == 0:
        q.pop()
    else:
        q.append(t)
print(sum(q))