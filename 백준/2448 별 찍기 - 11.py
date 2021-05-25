n = int(input())
map = [[" "] * (2 * n - 1) for _ in range(n)]
star = ["  *  ", " * * ", "*****"]


def fun(n, y, x):
    if n == 1:
        for i in range(3):
            for j in range(5):
                map[y + i][x + j] = star[i][j]
        return

    fun(n // 2, y, x + 3 * n // 2)
    fun(n // 2, y + 3 * n // 2, x)
    fun(n // 2, y + 3 * n // 2, x + 3 * n)


fun(n // 3, 0, 0)
for i in range(n):
    print("".join(map[i]))
