import sys
from collections import deque, defaultdict

input = sys.stdin.readline

if __name__ == "__main__":
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    ans = 0
    while True:
        outer_cheese = []
        outer_air = defaultdict(int)
        q = deque()
        q.append([0, 0])
        check = [[True] * m for _ in range(n)]
        check[0][0] = False
        while q:
            x, y = q.popleft()
            outer_air[str(x) + "_" + str(y)] += 1
            for i in range(4):
                new_x = x + dx[i]
                new_y = y + dy[i]
                if 0 <= new_x < n and 0 <= new_y < m and arr[new_x][new_y] == 0 and check[new_x][new_y]:
                    check[new_x][new_y] = False
                    q.append([new_x, new_y])

                if 0 <= new_x < n and 0 <= new_y < m and arr[new_x][new_y] == 1 and check[new_x][new_y]:
                    check[new_x][new_y] = False
                    outer_cheese.append([new_x, new_y])

        if not outer_cheese:
            break
        ans +=1

        for x, y in outer_cheese:
            cnt = 0
            for i in range(4):
                new_x = x + dx[i]
                new_y = y + dy[i]
                if 0 <= new_x < n and 0 <= new_y < m:
                    if outer_air[str(new_x) + "_" + str(new_y)] > 0:
                        cnt += 1
            if cnt > 1:
                arr[x][y] = 0
    print(ans)