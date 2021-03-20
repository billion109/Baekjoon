import sys

input = sys.stdin.readline


# 1의개수 세기
def count(N):
    cnt = 0
    while N != 0:
        N &= (N - 1)
        cnt += 1
    return cnt


if __name__ == "__main__":
    N, K = map(int, input().split())
    ans = 0
    while count(N) > K:
        ans += N & -N
        N += N & -N
    print(ans)