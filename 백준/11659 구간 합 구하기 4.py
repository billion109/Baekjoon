import sys
input = sys.stdin.readline


if __name__ == "__main__":
    N, M = map(int,input().split())
    arr = list(map(int,input().split()))
    dp = []
    for i in range(N):
        if i==0:
            dp.append(arr[0])
        else:
            dp.append(dp[-1]+arr[i])

    for _ in range(M):
        i,j = map(int,input().split())
        if i == 1:
            print(dp[j-1])
        else:
            print(dp[j-1]-dp[i-2])





