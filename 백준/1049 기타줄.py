import sys

input = sys.stdin.readline

if __name__ == "__main__":
    N, M = map(int, input().split())
    arr = []
    arr2 = []
    for i in range(M):
        x, y = map(int, input().split())
        arr.append([min(x, 6 * y), x, 6 * y])
        arr2.append(y)
        arr.sort()
        arr2.sort()

    ans = 0
    a = N // 6
    b = N % 6

    # 패키지가 더쌀떄
    if arr[0][0] == arr[0][1]:
        ans += a * arr[0][0]

        # 남은거 처리
        ans += min(arr[0][0], arr2[0] * b)

    else:
        ans += int(N * arr[0][0] / 6)

    print(ans)
