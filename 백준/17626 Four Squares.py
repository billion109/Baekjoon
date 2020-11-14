import sys
import math
input = sys.stdin.readline

N = int(input())

dp = [x for x in range(N+1)]
for i in range(N+1):
    if math.sqrt(i)==int(math.sqrt(i)):
        dp[i]=1


for i in range(N+1):
    for j in range(int(math.sqrt(i)+1)):
        dp[i] = min(dp[i], dp[j*j]+dp[i-j*j])

print(dp[N])
