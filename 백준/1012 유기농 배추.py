import sys
from collections import deque

T = int(sys.stdin.readline().rstrip())

for case in range(T):
    M,N,K = map(int, sys.stdin.readline().rstrip().split(' '))
    arr = [[0 for i in range(M)] for j in range(N)]
    for _ in range(K):
        x, y = map(int,sys.stdin.readline().rstrip().split(' '))
        arr[y][x] = 1

    visited = []
    ans = 0

    for j in range(N):
        for i in range(M):
            if arr[j][i] ==1 and ([j,i] not in visited):
                ans+=1
                stack = deque([[j,i]])
                while len(stack)>0:
                    temp = stack.popleft()
                    if temp in visited:
                        continue
                    visited.append(temp)
                    if temp[1]>0:
                        if arr[temp[0]][temp[1]-1]==1 and ([temp[0],temp[1]-1] not in visited):
                            stack.append([temp[0],temp[1]-1])
                    if temp[1]<M-1:
                        if arr[temp[0]][temp[1]+1]==1 and ([temp[0],temp[1]+1] not in visited):
                            stack.append([temp[0],temp[1]+1])
                    if temp[0]<N-1:
                        if arr[temp[0]+1][temp[1]]==1 and ([temp[0]+1,temp[1]] not in visited):
                            stack.append([temp[0]+1,temp[1]])
                    if temp[0]>0:
                        if arr[temp[0]-1][temp[1]]==1 and ([temp[0]-1,temp[1]]) not in visited:
                            stack.append([temp[0]-1,temp[1]])
    print(ans)