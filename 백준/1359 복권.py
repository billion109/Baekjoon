import sys

input = sys.stdin.readline
import math

if __name__ == "__main__":
    N, M, K = map(int, input().split())

    son = 1
    mom = 1
    for i in range(K):
        son *= (M - i)
        mom *= (N - i)

    ans = son*(10**10)
    ans /= mom
    ans /= 10**10
    print(ans)

