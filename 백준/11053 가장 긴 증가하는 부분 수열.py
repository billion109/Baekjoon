#https://seungkwan.tistory.com/8 참고

n = int(input())
arr = list(map(int,input().split()))
dp = [1]
for i in range(n-1):
    x = 0
    for j in range(i+1):
        if arr[j]<arr[i+1]:
            x = max(x,dp[j])
    dp.append(x+1)
print(max(dp))