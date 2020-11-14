import sys
from collections import deque
input= sys.stdin.readline

t = int(input())

for i in range(t):
    n,m = map(int, input().split(' '))
    arr = list(map(int, input().split(' ')))
    q = deque(arr)
    arr.sort(reverse=True)
    cnt = 1
    while True:
        temp = q.popleft()

        if m == 0:
            if temp == arr[0]:
                break
            else:
                q.append(temp)
                m = len(q)-1

        else:
            m -= 1
            if temp == arr[0]:
                arr.pop(0)
                cnt+=1
            else:
                q.append(temp)
    print(cnt)
