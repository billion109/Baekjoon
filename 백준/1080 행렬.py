import sys

input = sys.stdin.readline


def converse(a, b):
    for i in range(a, a + 3):
        for j in range(b, b + 3):
            if A[i][j] == 1:
                A[i][j] = 0
            else:
                A[i][j] = 1
    return


if __name__ == "__main__":
    N, M = map(int, input().split())
    A = [list(map(int,list(input().rstrip()))) for _ in range(N)]
    B = [list(map(int,list(input().rstrip()))) for _ in range(N)]
    ans = 0
    for i in range(N - 2):
        for j in range(M - 2):
            if A[i][j] == B[i][j]:
                continue
            else:
                converse(i, j)
                ans += 1

    check = True
    for i in range(N):
        for j in range(M):
            if A[i][j] != B[i][j]:
                check = False
                break

    if check:
        print(ans)
    else:
        print(-1)
