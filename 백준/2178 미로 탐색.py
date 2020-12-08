import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int,input().split())
arr = [input().rstrip() for _ in range(N)]
ans = [[0 for _ in range(M)] for _ in range(N)]
ans[0][0] = 1
q = deque([(0,0)])
xval = [1, -1, 0, 0]
yval = [0, 0, 1, -1]

while len(q)>0:
    x,y = q.popleft()
    for i in range(4):
        _x = x + xval[i]
        _y = y + yval[i]
        if 0 <= _x < N and 0 <= _y < M:
            if arr[_x][_y] == '1':
                if ans[_x][_y]==0:
                    q.append((_x,_y))
                    ans[_x][_y] = ans[x][y]+1

print(ans[N-1][M-1])
