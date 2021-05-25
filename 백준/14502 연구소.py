import sys, copy
from itertools import combinations
from collections import deque

input = sys.stdin.readline


def solution(n, m, board):
    virus_pos = []
    wall_pos = []
    empty_pos = []
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    for i in range(n):
        for j in range(m):
            if board[i][j] == 0:
                empty_pos.append([i, j])
            elif board[i][j] == 1:
                wall_pos.append([i, j])
            elif board[i][j] == 2:
                virus_pos.append([i, j])

    ans = 0
    new_wall = list(combinations(empty_pos, 3))
    for i in range(len(new_wall)):
        new_board = copy.deepcopy(board)
        for x, y in new_wall[i]:
            new_board[x][y] = 1

        check = [[True] * m for _ in range(n)]
        for x, y in virus_pos:
            dq = deque()
            check[x][y] = False
            dq.append([x, y])
            while dq:
                x_pos, y_pos = dq.popleft()
                for j in range(4):
                    new_x = x_pos + dx[j]
                    new_y = y_pos + dy[j]
                    if 0 <= new_x < n and 0 <= new_y < m and new_board[new_x][new_y] == 0 and check[new_x][new_y]:
                        check[new_x][new_y] = False
                        new_board[new_x][new_y] = 2
                        dq.append([new_x, new_y])

        tmp = 0
        for x in range(n):
            for y in range(m):
                if new_board[x][y] == 0:
                    tmp+=1

        ans = max(ans,tmp)

    print(ans)



if __name__ == "__main__":
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    solution(n, m, board)
