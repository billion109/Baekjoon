import sys, copy
input = sys.stdin.readline
from collections import deque

# 이거 내부치즈는 공기취급안해야하는데 그걸못봤네
if __name__ == "__main__":
    N, M = map(int, input().split())
    board = []
    ans = 0
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    q = deque()
    for i in range(N):
        temp = list(map(int, input().split()))
        for j in range(M):
            if temp[j] == 1:
                q.append([i, j])
        board.append(temp)

    temp = deque()
    new_board = copy.deepcopy(board)
    while q:
        x, y = q.popleft()
        cnt = 0
        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]
            if board[new_x][new_y] == 0:
                cnt += 1
        if cnt >= 2:
            new_board[x][y] = 0
        else:
            temp.append([x, y])

        if not q:
            ans += 1
            q = temp
            temp = deque()
            board = copy.deepcopy(new_board)

    print(ans)
