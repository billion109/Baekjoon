import sys
from collections import deque
sys.setrecursionlimit(50000)


input = sys.stdin.readline
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y):
    more_edge = True

    if x == N - 1 and y == M - 1:
        topological.appendleft([x, y])
        return

    for i in range(4):
        pos_x = x + dx[i]
        pos_y = y + dy[i]
        if 0 <= pos_x < N and 0 <= pos_y < M and arr[y][x] > arr[pos_y][pos_x] \
                and check[pos_y][pos_x]:
            check[pos_y][pos_x] = False
            more_edge = False
            dfs(pos_x, pos_y)
    topological.appendleft([x, y])
    return


if __name__ == "__main__":
    # M이 세로, N이 가로
    M, N = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(M)]
    check = [[True]*N for _ in range(M)]
    check[0][0] = True
    stack = deque([])
    stack.append([0, 0])
    topological = deque([])
    dfs(0, 0)

    dp = [[0]*N for _ in range(M)]
    dp[0][0]=1
    check = [[True]* N for _ in range(M)]
    check[0][0] = False
    for x, y in topological:
        check[y][x] = False
        for i in range(4):
            pos_x = x + dx[i]
            pos_y = y + dy[i]

            if 0 <= pos_x < N and 0 <= pos_y < M and arr[y][x] > arr[pos_y][pos_x] \
                    and check[pos_y][pos_x]:
                dp[pos_y][pos_x] += dp[y][x]

    print(dp[-1][-1])
