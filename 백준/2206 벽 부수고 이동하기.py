import sys
from collections import deque

input = sys.stdin.readline

if __name__ == "__main__":
    N, M = map(int, input().split())
    stack = deque([])
    arr = []
    for _ in range(N):
        arr.append(list(map(int, list(input().rstrip()))))

    check = [[[False] * M for _ in range(N)] for _ in range(2)]
    stack.append([[0, 0], 0, 1])
    check[1][0][0] = True
    move = [[1, 0], [-1, 0], [0, 1], [0, -1]]

    while len(stack) > 0:
        # print(stack)
        pos, dist, destroy = stack.popleft()
        if pos[0] == N - 1 and pos[1] == M - 1:
            print(dist + 1)
            exit(0)
        if destroy > 0:
            for dx, dy in move:
                x = pos[0] + dx
                y = pos[1] + dy
                if 0 <= x < N and 0 <= y < M and check[destroy][x][y] == False and arr[x][y] == 1:
                    check[destroy][x][y] = True
                    stack.append([[x, y], dist + 1, destroy - 1])

        for dx, dy in move:
            x = pos[0] + dx
            y = pos[1] + dy

            if 0 <= x < N and 0 <= y < M and check[destroy][x][y] == False and arr[x][y] == 0:
                check[destroy][x][y] = True
                stack.append([[x, y], dist + 1, destroy])

    print(-1)
