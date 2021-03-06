import sys
from collections import deque

input = sys.stdin.readline

if __name__ == "__main__":
    K = int(input())
    W, H = map(int, input().split())
    if W == 1 and H == 1:
        print(0)
        exit(0)

    arr = []
    for i in range(H):
        arr.append(list(map(int, input().split())))

    stack = deque([])
    check = [[[False] * W for _ in range(H)] for _ in range(K+1)]
    stack.append([[0, 0], K, 0])
    check[K][0][0] = True
    horse_move = [[-2, -1], [-1, -2], [1, -2], [2, -1], [-2, 1], [-1, 2], [1, 2], [2, 1]]
    move = [[1, 0], [0, 1], [-1, 0], [0, -1]]

    while len(stack) > 0:
        pos, curr_K, cnt = stack.popleft()
        #print(pos, curr_K, cnt,stack)
        if pos[0] == W - 1 and pos[1] == H - 1:
            print(cnt)
            exit(0)
        if curr_K > 0:
            for dx, dy in horse_move:
                x = pos[0] + dx
                y = pos[1] + dy
                if 0 <= x < W and 0 <= y < H and check[curr_K-1][y][x] == False and arr[y][x] == 0:
                    check[curr_K-1][y][x] = True
                    stack.append([[x, y], curr_K - 1, cnt + 1])

        for dx, dy in move:
            x = pos[0] + dx
            y = pos[1] + dy
            if 0 <= x < W and 0 <= y < H and check[curr_K][y][x] == False and arr[y][x] == 0:
                check[curr_K][y][x] = True
                stack.append([[x, y], curr_K, cnt + 1])

    print(-1)
