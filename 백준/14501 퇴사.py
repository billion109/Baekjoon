import sys

input = sys.stdin.readline


def fun(day, val):
    tmp = []
    if day + arr[day - 1][0] - 1 > n:
        return val
    val += arr[day - 1][1]
    day += arr[day - 1][0]

    for i in range(day, n + 1):
        tmp.append(fun(i, val))

    if len(tmp) == 0:
        return val
    return max(tmp)


if __name__ == "__main__":
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    ans = 0

    for i in range(n):
        ans = max(fun(i + 1, 0), ans)

    print(ans)
