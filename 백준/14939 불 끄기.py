import sys

input = sys.stdin.readline

if __name__ == "__main__":
    arr = [list(input().rstrip()) for _ in range(10)]
    dx = [0, 1, 1, 1, 2]
    dy = [0, -1, 0, 1, 0]
    ans = 0
    for i in range(10):
        for j in range(10):
            if arr[i][j] == 'O':
                ans +=1
                for k in range(5):
                    x = i + dx[k]
                    y = j + dy[k]
                    if 0 <= x < 10 and 0 <= y < 10:
                        if arr[x][y] == 'O':
                            arr[x][y] = '#'
                        elif arr[x][y] == '#':
                            arr[x][y] = 'O'

    for i in range(10):
        for j in range(10):
            if arr[i][j] == 'O':
                print(-1)
                exit(0)

    print(ans)
