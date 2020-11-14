import sys
from collections import Counter

n = int(input())
if n==1:
    x = int(input())
    print(x)
    print(x)
    print(x)
    print(0)
else:

    arr = []
    sum = 0
    for _ in range(n):
        m = int(sys.stdin.readline())
        arr.append(m)
        sum+=m

    arr.sort()
    cnt = Counter(arr)
    cnt = sorted(cnt.items(), key=lambda x: (-x[1],x[0]))
    print(round(sum/n))
    print(arr[int((n-1)/2)])
    if cnt[0][1] == cnt[1][1]:
        print(cnt[1][0])
    else:
        print(cnt[0][0])
    print(arr[-1]-arr[0])
