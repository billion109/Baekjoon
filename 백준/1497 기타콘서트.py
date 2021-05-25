import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**5)


def fun(guitar, cnt, check):
    global ans
    if cnt>=ans:
        return

    for k in range(M):
        if arr[guitar][k] == 'Y':
            check[k] = 1

    if sum(check) == M:
        ans = min(cnt, ans)
        return

    for i in range(guitar+1, N):
        fun(i, cnt+1, check[:])




if __name__ == "__main__":
    N, M = map(int, input().split())
    arr = []
    for i in range(N):
        x, y = input().split()
        arr.append(list(y))

    ans = 11
    check = [0] * M
    for i in range(N):
        fun(i, 1, check[:])

    if ans==11:
        print(-1)
    else:
        print(ans)

