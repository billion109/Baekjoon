import sys
from collections import deque
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    dp = [0 for i in range(n+1)]
    q = deque()
    q.append([n,[n]])

    while q:
        curr, curr_list = q.popleft()
        if curr == 1:
            print(dp[1])
            print(*curr_list)
            break

        if curr%3 == 0:
            if dp[curr//3] ==0:
                dp[curr//3] += dp[curr]+1
                q.append([curr//3, curr_list+[curr//3]])

        if curr%2 == 0:
            if dp[curr//2]==0:
                dp[curr//2] += dp[curr]+1
                q.append([curr//2, curr_list+[curr//2]])

        if dp[curr-1]==0:
            dp[curr-1] += dp[curr]+1
            q.append([curr-1,curr_list+[curr-1]])






