from bisect import bisect_left
from collections import deque

N = int(input())
arr = list(map(int, input().split()))


def main():
    if N == 1:
        print(1)
        print(arr[0])
        return

    dp = [arr[0]]
    ans = [[]for _ in range(N)]
    ans[0].append(0)

    for i in range(1, N):
        if dp[-1] < arr[i]:
            dp.append(arr[i])
            ans[len(dp)-1].append(i)

        else:
            temp = bisect_left(dp, arr[i])
            dp[temp] = arr[i]
            ans[temp].append(i)

    print(len(dp))

    ans2 = deque([])
    for i in reversed(range(len(dp))):
        if i == len(dp)-1:
            max_val = max(ans[i])
            ans2.appendleft(max_val)
        else:
            temp = []
            for j in ans[i]:
                if j<max_val:
                    temp.append(j)
            max_val = max(temp)
            ans2.appendleft(max_val)
    for i in ans2:
        print(arr[i], end=' ')



if __name__ == "__main__":
    main()
