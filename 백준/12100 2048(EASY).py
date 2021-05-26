import sys
import copy
from collections import deque

input = sys.stdin.readline


def up(board, n):
    board2 = []
    for i in range(n):
        tmp = []
        for j in range(n):
            tmp.append(board[j][i])
        board2.append(tmp)

    for i in range(n):
        tmp = []
        q = deque()
        for j in range(n):
            if board2[i][j] == 0:
                continue

            if q:
                if q[-1] == board2[i][j]:
                    q[-1] *= 2
                    tmp += q
                    q.clear()
                else:
                    q.append(board2[i][j])
            else:
                q.append(board2[i][j])
        tmp += q

        while len(tmp) != n:
            tmp.append(0)

        board2[i] = tmp
    for i in range(n):
        for j in range(i + 1, n):
            board2[i][j], board2[j][i] = board2[j][i], board2[i][j]
    return board2


def down(board, n):
    board2 = []
    for i in range(n):
        tmp = []
        for j in range(n):
            tmp.append(board[j][i])
        board2.append(tmp)

    for i in range(n):
        tmp = deque()
        q = deque()
        for j in reversed(range(n)):
            if board2[i][j] == 0:
                continue

            if q:
                if q[0] == board2[i][j]:
                    q[0] *= 2
                    tmp = q + tmp
                    q.clear()
                else:
                    q.appendleft(board2[i][j])
            else:
                q.appendleft(board2[i][j])
        tmp = q + tmp

        while len(tmp) != n:
            tmp.appendleft(0)

        board2[i] = tmp

    for i in range(n):
        for j in range(i + 1, n):
            board2[i][j], board2[j][i] = board2[j][i], board2[i][j]
    return board2


def left(board, n):
    for i in range(n):
        tmp = []

        q = deque()
        for j in range(n):
            if board[i][j] == 0:
                continue

            if q:
                if q[-1] == board[i][j]:
                    q[-1] *= 2
                    tmp += q
                    q.clear()
                else:
                    q.append(board[i][j])
            else:
                q.append(board[i][j])
        tmp += q

        while len(tmp) != n:
            tmp.append(0)

        board[i] = tmp
    return board


def right(board, n):
    for i in range(n):
        tmp = deque()
        q = deque()
        for j in reversed(range(n)):
            if board[i][j] == 0:
                continue

            if q:
                if q[0] == board[i][j]:
                    q[0] *= 2
                    tmp = q + tmp
                    q.clear()
                else:
                    q.appendleft(board[i][j])
            else:
                q.appendleft(board[i][j])
        tmp = q + tmp

        while len(tmp) != n:
            tmp.appendleft(0)

        board[i] = tmp

    return board


if __name__ == "__main__":
    move = [up, down, left, right]
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    move_list = []
    ans = 0
    for i in range(4):
        for j in range(4):
            for k in range(4):
                for u in range(4):
                    for v in range(4):
                        move_list.append([i, j, k, u, v])

    for moves in move_list:
        new_board = copy.deepcopy(board)

        for i in moves:
            new_board = move[i](new_board, n)
            # if moves == [3,3,3,3,1]:
            #     print('---------' + str(i))
            #     for j in range(n):
            #         print(*new_board[j])

        ans = max(max(map(max, new_board)), ans)
    print(ans)
"""
5
2 2 4 8 16
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
2 2 4 8 16

5
16 8 4 2 2 
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
16 8 4 2 2
"""
