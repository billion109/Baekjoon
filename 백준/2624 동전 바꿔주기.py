import sys
import copy
input = sys.stdin.readline


def fun(dp, curr, remain):
    pass


if __name__ == "__main__":
    t = int(input())
    k = int(input())
    arr = []
    for i in range(k):
        arr.append(list(map(int, input().split())))
    arr.sort()
    dp = [[0] * (t + 1) for _ in range(k)]
    for i in range(k):
        if i == 0:
            for j in range(1, arr[i][1] + 1):
                if j * arr[i][0] <= t:
                    dp[i][j * arr[i][0]] = 1
                else:
                    break
        else:
            dp[i] = copy.deepcopy(dp[i-1])
            for j in range(1, t + 1):
                if dp[i - 1][j] != 0:
                    for x in range(1,arr[i][1]+1):
                        if j + x * arr[i][0] <= t:
                            dp[i][j + x * arr[i][0]] += dp[i - 1][j]
                        else:
                            break
            for j in range(1, arr[i][1] + 1):
                if arr[i][0] * j <= t:
                    dp[i][j * arr[i][0]] += 1
                else:
                    break

    print(dp[-1][-1])
