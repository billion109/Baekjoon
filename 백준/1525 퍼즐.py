import sys, copy
from collections import defaultdict, deque

input = sys.stdin.readline
dx = [-1, 1, -3, 3]
answer = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]


def find_blank(arr):
    for i in range(3):
        for j in range(3):
            if arr[i][j] == 0:
                return [i, j]


def list_to_str(arr):
    string = ""
    for i in range(3):
        for j in range(3):
            string += str(arr[i][j])
    return string


def main():
    arr = [list(map(int, input().split())) for _ in range(3)]
    check = defaultdict(int)
    q = deque()
    q.append([list_to_str(arr), 0])
    check[list_to_str(arr)] += 1

    while q:
        board, cnt = q.popleft()
        if board == "123456780":
            print(cnt)
            return

        blank = board.index('0')
        for i in range(4):
            new_blank = blank + dx[i]
            if blank % 3 == 2 and i == 1:
                continue
            if blank % 3 == 0 and i == 0:
                continue

            if 0 <= new_blank < 9:
                new_board = list(board[:])
                new_board[blank] = board[new_blank]
                new_board[new_blank] = board[blank]
                new_board = "".join(new_board)

                if check[new_board] == 0:
                    q.append([new_board, cnt + 1])
                    check[new_board] += 1
    print(-1)
    return


main()
