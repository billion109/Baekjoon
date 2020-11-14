import sys
from collections import deque
input = sys.stdin.readline

S = input().rstrip()
arr = deque([])
flag = 0
for i in range(len(S)):
    if S[i]=='+' or S[i]=='-':
        arr.append(int(S[flag:i]))
        arr.append(S[i])
        flag=i+1
arr.append(int(S[flag:]))

q = deque([])
while len(arr)>0:
    i = arr.popleft()
    if i=='+':
        q.append(q.pop()+arr.popleft())
    else:
        q.append(i)
ans = q.popleft()
while len(q)>0:
    i = q.popleft()
    if i!='-':
        ans-=i

print(ans)
