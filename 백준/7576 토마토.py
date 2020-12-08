import sys
input = sys.stdin.readline
from collections import deque

M,N = map(int,input().split())
BOX_SIZE = M*N
tomato_unmature = 0
tomato_box = []
day = 0

tomato_q = deque([])
q = deque([])

for i in range(N):
    temp = input().split()
    tomato_box.append(temp)
    for j in range(M):
        if temp[j]== '0':
            tomato_unmature+=1
        elif temp[j] == '1':
            tomato_q.append([i,j])

if tomato_unmature==0:
    print(0)
else:
    while len(tomato_q)>0:
        q = tomato_q.copy()
        tomato_q.clear()

        while len(q)>0:
            x,y = q.popleft()
            if x>0:
                if tomato_box[x-1][y] == '0':
                    tomato_box[x-1][y] = '1'
                    tomato_q.append([x-1,y])
                    tomato_unmature-=1

            if x<N-1:
                if tomato_box[x+1][y] == '0':
                    tomato_box[x+1][y] = '1'
                    tomato_q.append([x+1,y])
                    tomato_unmature -= 1
            if y > 0:
                if tomato_box[x][y-1] == '0':
                    tomato_box[x][y-1] = '1'
                    tomato_q.append([x,y-1])
                    tomato_unmature -= 1

            if y < M - 1:
                if tomato_box[x][y+1] == '0':
                    tomato_box[x][y+1] = '1'
                    tomato_q.append([x, y+1])
                    tomato_unmature -= 1

        day+=1

    if tomato_unmature==0:
        print(day-1)
    else:
        print(-1)