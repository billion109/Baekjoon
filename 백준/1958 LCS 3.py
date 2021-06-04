import sys

input = sys.stdin.readline

str1 = input().rstrip()
str2 = input().rstrip()
str3 = input().rstrip()
dp = [[[0] * (len(str1) + 1) for _ in range(len(str2) + 1)] for _ in range(len(str3)+1)]
for k in range(1, len(str3)+1):
    for i in range(1, len(str2) + 1):
        for j in range(1, len(str1) + 1):
            if str1[j-1] == str2[i-1] and str1[j-1] == str3[k-1]:
                dp[k][i][j] = dp[k-1][i-1][j-1]+1
            else:
                dp[k][i][j] = max(dp[k][i-1][j], dp[k][i][j-1], dp[k-1][i][j])
print(dp[-1][-1][-1])

