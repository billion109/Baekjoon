import sys

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))
    dp1 = [arr1[0]]
    dp2 = [arr2[0]]

    if n == 1:
        print(max(dp1[-1], dp2[-1]))
    else:
        dp1.append(arr1[1] + dp2[0])
        dp2.append(arr2[1] + dp1[0])
        if n == 2:
            print(max(dp1[-1], dp2[-1]))
        else:
            for i in range(2, n):
                dp1.append(max(dp2[i - 1], dp2[i - 2]) + arr1[i])
                dp2.append(max(dp1[i - 1], dp1[i - 2]) + arr2[i])
            print(max(dp1[-1], dp2[-1]))
    #print(dp1)
    #print(dp2)
