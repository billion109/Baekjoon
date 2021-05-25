import sys

input = sys.stdin.readline
from collections import deque
from collections import defaultdict

if __name__ == "__main__":
    n, m = map(int, input().split())
    arr = []
    for i in range(n):
        arr.append(list(map(int, input().split())))
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    q = deque()
    check = [[True] * m for _ in range(n)]
    val = 0
    val_list = []

    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1 and check[i][j]:
                val += 1
                q.append([i, j])
                check[i][j] = False
                arr[i][j] = val
                cnt = 1
                while q:
                    x, y = q.popleft()
                    for k in range(4):
                        new_x = x + dx[k]
                        new_y = y + dy[k]
                        if 0 <= new_x < n and 0 <= new_y < m and check[new_x][new_y]:
                            if arr[new_x][new_y] == 1:
                                check[new_x][new_y] = False
                                q.append([new_x, new_y])
                                arr[new_x][new_y] = val
                                cnt += 1

                val_list.append([val, cnt])

    ans = 0

    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0:
                temp = []
                for k in range(4):
                    new_x = i + dx[k]
                    new_y = j + dy[k]
                    if 0 <= new_x < n and 0 <= new_y < m and arr[new_x][new_y] !=0:
                        temp.append(arr[new_x][new_y])
                if temp:
                    temp = list(set(temp))
                    temp2 = 0
                    for x in temp:
                        temp2 +=val_list[x-1][1]

                    ans = max(temp2,ans)

    print(ans+1)
