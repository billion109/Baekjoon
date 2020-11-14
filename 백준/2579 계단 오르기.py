import sys
input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]
dp = []

def fun():
    if n==1:
        print(arr[0])
        return
    elif n==2:
        print(arr[0]+arr[1])
        return
    elif n==3:
        print(max(arr[0]+arr[2], arr[1]+arr[2]))
        return
    else:
        dp.append(arr[0])
        dp.append(arr[0]+arr[1])
        dp.append(max(arr[0]+arr[2], arr[1]+arr[2]))
        for i in range(3,n):
            dp.append(max(dp[i-2]+arr[i], dp[i-3]+arr[i-1]+arr[i]))
        print(dp[n-1])
        return


fun()