import sys
from collections import deque

input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    ans = 0
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    for i in range(n):
        for j in range(n):
            q = deque()
            q.append([i, j, 1])
            check = [[0] * n for _ in range(n)]
            check[i][j] = 1
            while q:
                x, y, day = q.pop()
                for i in range(4):
                    next_x = x+dx[i]
                    next_y = y+dy[i]
                    if 0<=next_x<n and 0<=next_y<n:
                        pass

