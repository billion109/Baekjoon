T = int(input())

dp = [1,2,4]
arr = []

for i in range(T):
    arr.append(int(input()))

max_val = max(arr)

for i in range(3,max_val):
    dp.append(dp[i-3]+dp[i-2]+dp[i-1])

for i in arr:
    print(dp[i-1])