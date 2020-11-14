from _collections import deque
import sys

n = int(input())
q = deque([])
for _ in range(n):
    command = sys.stdin.readline().rstrip().split(' ')
    if command[0] == 'push':
        q.append(command[1])
    elif command[0] == 'top':
        if len(q)==0:
            print(-1)
        else:
            print(q[-1])
    elif command[0] == 'size':
        print(len(q))
    elif command[0] =='pop':
        if len(q)==0:
            print(-1)
        else:
            print(q.pop())
    elif command[0] =='empty':
        if len(q)==0:
            print(1)
        else:
            print(0)
    else:
        print(command)
        print('error')