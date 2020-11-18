import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
arr = []
q = deque([[0,0,N]])
a1, a2, a3 = 0,0,0
for i in range(N):
    arr.append(list(map(int, input().split())))

while len(q)>0:
    x,y,l = q.popleft()
    s = set()
    for i in range(x,x+l):
        for j in range(y,y+l):
            s.add(arr[i][j])
        if len(s)>1:
            break

    if len(s)==1:
        t = s.pop()
        if t == -1:
            a1+=1
        elif t == 0:
            a2+=1
        elif t == 1:
            a3+=1
    else:
        l = l//3
        q.append([x,y,l])
        q.append([x+l, y, l])
        q.append([x+2*l, y, l])
        q.append([x, y+l, l])
        q.append([x+l, y+l, l])
        q.append([x+2*l, y+l, l])
        q.append([x, y+2*l, l])
        q.append([x+l, y+2*l, l])
        q.append([x+2*l, y+2*l, l])

print(a1)
print(a2)
print(a3)