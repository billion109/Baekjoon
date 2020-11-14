n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int,input().split())))

for i in range(n-1):
    dp = []

    for j in range(len(arr[n-i-1])-1):
        dp.append(max(arr[n-i-1][j],arr[n-i-1][j+1]))
        dp[j]+=arr[n-i-2][j]
    arr[n-i-2] = dp

print(arr[0][0])