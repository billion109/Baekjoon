import sys
from collections import deque

INF = sys.maxsize
input = sys.stdin.readline

if __name__ == "__main__":
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    ans = INF
    n = int(input())
    board = [input().rstrip() for _ in range(n)]
    check_board = [[[True for i in range(n)] for j in range(n)] for k in range(2 * n)]
    q = deque()
    q.append([0, 0, 0])
    check_board[0][0][0] = False
    while q:
        cnt, x, y = q.popleft()
        if cnt > ans:
            continue

        if x == n - 1 and y == n - 1:
            ans = min(ans, cnt)
            continue

        for k in range(4):
            new_x = x + dx[k]
            new_y = y + dy[k]
            if 0 <= new_x < n and 0 <= new_y < n:
                if board[new_x][new_y] == '1':
                    if check_board[cnt][new_x][new_y]:
                        check_board[cnt][new_x][new_y] = False
                        q.append([cnt, new_x, new_y])
                else:
                    if check_board[cnt + 1][new_x][new_y]:
                        check_board[cnt + 1][new_x][new_y] = False
                        q.append([cnt+1, new_x, new_y])

    print(ans)
