n = int(input())
mod = 1000000000
dp = [[0] * 10 for _ in range(n)]
for i in range(1, 10):
    dp[0][i] = 1

for i in range(1, n):
    for j in range(10):
        if j > 0:
            dp[i][j] = (dp[i][j] + dp[i - 1][j - 1])%mod

        if j < 9:
            dp[i][j] = (dp[i][j]+dp[i - 1][j + 1])%mod

print(sum(dp[-1])%mod)
