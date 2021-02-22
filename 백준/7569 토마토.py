import sys
from collections import deque

input = sys.stdin.readline

m, n, h = map(int, input().split())
box = []
box_check = [[[False] * m for _ in range(n)] for __ in range(h)]
q = deque([])
dxyz = [(-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)]
not_mature_num = 0

for k in range(h):
    temp = []
    for j in range(n):
        temp2 = list(map(int, input().split()))
        for i in range(m):
            if temp2[i] == 0:
                not_mature_num += 1
            elif temp2[i] == 1:
                q.append((i, j, k))
                box_check[k][j][i] = True

        temp.append(temp2)
    box.append(temp)


def bfs():
    global not_mature_num
    time = 0

    if not_mature_num == 0:
        print(0)
        return

    while len(q) > 0:
        x, y, z = q.popleft()
        for dx, dy, dz in dxyz:
            nx = x + dx
            ny = y + dy
            nz = z + dz

            if 0 <= nx < m and 0 <= ny < n and 0 <= nz < h and (box_check[nz][ny][nx] == False) \
                    and box[nz][ny][nx] == 0:
                q.append((nx, ny, nz))
                box_check[nz][ny][nx] = True
                box[nz][ny][nx] = box[z][y][x] + 1
                time = max(box[z][y][x] + 1, time)
                not_mature_num -= 1

    if not_mature_num != 0:
        print(-1)
        return
    '''
    for k in range(h):
        for j in range(n):
            for i in range(m):
                print(box[k][j][i], end=' ')
            print()
    '''
    print(time - 1)


bfs()
