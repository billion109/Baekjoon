import sys

input = sys.stdin.readline

str1 = input().rstrip()
str2 = input().rstrip()

dp = [[0] * (len(str1) + 1) for _ in range(len(str2) + 1)]
for i in range(1, len(str2) + 1):
    for j in range(1, len(str1) + 1):
        if str1[j-1] == str2[i-1]:
            dp[i][j] = dp[i-1][j-1]+1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
print(dp[-1][-1])

'''
for i in range(len(str2)+1):
    for j in range(len(str1)+1):
        print(dp[i][j],end= ' ')
    print()
'''

#https://ko.wikipedia.org/wiki/%EC%B5%9C%EC%9E%A5_%EA%B3%B5%ED%86%B5_%EB%B6%80%EB%B6%84_%EC%88%98%EC%97%B4
