n = int(input())
dp = [[0 for _ in range(1 << 10)] for _ in range(10)]
mod = 1000000000

for i in range(1, 10):
    dp[i][1 << i] = 1

for i in range(1, n):
    new_dp = [[0 for _ in range(1 << 10)] for _ in range(10)]
    for e in range(10):
        for bm in range(1 << 10):
            if e < 9:
                new_dp[e][bm | (1 << e)] += dp[e + 1][bm]
                new_dp[e][bm | (1 << e)] %= mod
            if e > 0:
                new_dp[e][bm | (1 << e)] += dp[e - 1][bm]
                new_dp[e][bm | (1 << e)] %= mod
    dp = new_dp

print(sum([dp[i][1023] for i in range(10)]) % mod)
