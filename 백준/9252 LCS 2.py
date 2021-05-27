import sys

input = sys.stdin.readline

str1 = input().rstrip()
str2 = input().rstrip()

dp = [[0] * (len(str1) + 1) for _ in range(len(str2) + 1)]
for i in range(1, len(str2) + 1):
    for j in range(1, len(str1) + 1):
        if str1[j - 1] == str2[i - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
print(dp[-1][-1])
if dp[-1][-1] != 0:
    row = len(str2)
    col = len(str1)
    ans = ""
    while row > 0 and col > 0:
        if str1[col-1] == str2[row-1]:
            ans = str1[col-1] + ans
            row -= 1
            col -= 1
        else:
            if dp[row - 1][col] >= dp[row][col - 1]:
                row -= 1
            else:
                col-=1
    print(ans)
