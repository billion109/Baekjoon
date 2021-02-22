import sys
from math import lcm

input = sys.stdin.readline
MAX_ANS = 10000000000
n = int(input())
for i in range(n):
    M, N, x, y = map(int, input().split())
    flag = False
    ans = MAX_ANS
    max_val = lcm(M, N)
    val = x
    while val <= max_val:
        if val % N == y or (N == y and val % N == 0):
            ans = min(val, ans)
            break
        val += M

    if ans == MAX_ANS:
        print(-1)
    else:
        print(ans)
