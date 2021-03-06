import sys
from bisect import bisect_left
input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    arr = list(map(int, input().split()))
    dp = []

    if N == 1:
        print(1)
        exit(0)

    dp.append(arr[0])
    for i in range(1, N):
        if dp[-1] < arr[i]:
            dp.append(arr[i])

        else:
            '''
            left = 0
            right = len(dp) - 1
            while left <= right:
                mid = (left + right) // 2
                if dp[mid] == arr[i]:
                    break
                elif dp[mid] > arr[i]:
                    right = mid - 1
                else:
                    left = mid + 1
            if right < left:
                dp[left] = arr[i]
            '''
            dp[bisect_left(dp,arr[i])] = arr[i]
    print(len(dp))
