dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

r, c = map(int, input().split())
arr = []
for _ in range(r):
    arr.append(input().rstrip())

new_arr = []
for i in range(r):
    temp = ''
    for j in range(c):
        if arr[i][j] == 'X':
            cnt = 0
            for k in range(4):
                x = i + dx[k]
                y = j + dy[k]
                if 0 <= x < r and 0 <= y < c and arr[x][y] == 'X':
                    cnt += 1
            if cnt > 1:
                temp += 'X'
            else:
                temp += '.'
        else:
            temp += '.'
    new_arr.append(temp)

sx, sy = r - 1, c - 1
ex, ey = 0, 0
for i in range(r):
    for j in range(c):
        if new_arr[i][j] == 'X':
            sx = min(sx,i)
            sy = min(sy,j)
            ex = max(ex,i)
            ey = max(ey,j)

for i in range(sx,ex+1):
    for j in range(sy,ey+1):
        print(new_arr[i][j],end='')
    print()
