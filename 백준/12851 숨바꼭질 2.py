import sys

input = sys.stdin.readline
from collections import deque

if __name__ == "__main__":
    N, K = map(int, input().split())
    q = deque([N])


    check = [-1] * 100001
    check[N] = 0

    ans = [0] * 100001
    ans[N] = 1

    if N == K:
        print(0)
        print(1)
        exit(0)

    while q:
        curr = q.popleft()
        for i in (2 * curr, curr - 1, curr + 1):
            if 0 <= i <= 100000:
                if check[i] == -1:
                    q.append(i)
                    check[i] = check[curr]+1
                    ans[i] = ans[curr]

                elif check[i] == check[curr]+1:
                    ans[i] += ans[curr]

    print(check[K])
    print(ans[K])
