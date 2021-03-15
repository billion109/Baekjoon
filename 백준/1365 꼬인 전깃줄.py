import sys
from bisect import bisect_left
input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input().rstrip())
    arr = list(map(int,input().split()))
    dp = [arr[0]]
    for i in range(1,N):
        if arr[i] > dp[-1]:
            dp.append(arr[i])
        else:
            dp[bisect_left(dp,arr[i])] = arr[i]

    print(N-len(dp))
