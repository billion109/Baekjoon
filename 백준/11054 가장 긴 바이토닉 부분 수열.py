import sys

input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    arr = list(map(int, input().split()))
    arr_reversed = list(reversed(arr))
    ascend = [0] * N
    descend = [0] * N

    if N == 1:
        print(1)
        exit(0)

    # 오름차순부터
    dp = []
    ascend[0] = 1
    dp.append(arr[0])
    for i in range(1, N):
        if dp[-1] < arr[i]:
            dp.append(arr[i])
            ascend[i] = len(dp)

        else:
            for j in range(N):
                if arr[i] <= dp[j]:
                    dp[j] = arr[i]
                    ascend[i] = j + 1
                    break
                else:
                    continue

    # 내림차순
    dp = []
    descend[0] = 1
    dp.append(arr_reversed[0])
    for i in range(1, N):
        if dp[-1] < arr_reversed[i]:
            dp.append(arr_reversed[i])
            descend[i] = len(dp)

        else:
            for j in range(N):
                if arr_reversed[i] <= dp[j]:
                    dp[j] = arr_reversed[i]
                    descend[i] = j + 1
                    break
                else:
                    continue

    descend = list(reversed(descend))
    temp = [ascend[i]+descend[i] for i in range(N)]
    print(max(temp)-1)