import sys
from collections import deque

input = sys.stdin.readline
s = [0]
n = int(input())
q = deque([x+1 for x in range(n)])
ans = []
flag = True
for i in range(n):
    v = int(input())
    while True:
        if v==s[-1]:
            s.pop()
            ans.append('-')
            break
        elif v>s[-1]:
            s.append(q.popleft())
            ans.append('+')
        else:
            if v<s[-1]:
                flag = False
                break
if flag==False:
    print('NO')
else:
    for i in ans:
        print(i)
