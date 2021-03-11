import sys

input = sys.stdin.readline

if __name__ == "__main__":
    n, k = map(int, input().split())
    item = [list(map(int, input().split())) for _ in range(n)]
    dp = [[0]*(k+1) for _ in range(n+1)]

    for i in range(1, n+1):
        for w in range(1, k+1):
            if item[i-1][0] > w:
                dp[i][w] = dp[i-1][w]
            else:
                dp[i][w] = max(dp[i-1][w], dp[i-1][w-item[i-1][0]]+item[i-1][1])

    print(dp[-1][-1])



