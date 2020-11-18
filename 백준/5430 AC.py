import sys
input = sys.stdin.readline
from collections import deque

T = int(input())
for _ in range(T):
    p = input().rstrip()
    n = int(input())
    temp = input()[1:-2]
    if n==0:
        arr=[]
    else:
        arr = temp.split(',')
    q = deque(arr)
    flag = 0
    sw = 0
    for x in p:
        if x == 'R':
            if sw == 0:
                sw=1
            else:
                sw = 0

        else:
            if len(q)==0:
                flag=1
                break
            else:
                if sw == 0:
                    q.popleft()
                else:
                    q.pop()
    if flag==0:
        if sw==0:
            print('[',end='')
            print(','.join(list(q)),end='')
            print(']')
        else:
            q.reverse()
            print('[',end='')
            print(','.join(list(q)),end='')
            print(']')
    else:
        print('error')