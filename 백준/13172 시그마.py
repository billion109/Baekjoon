import sys

input = sys.stdin.readline


def mul(x, y, p):
    ans = 1
    while y > 0:
        if (y % 2 != 0):
            ans *= x
            ans %= p
        x *= x
        x %= p
        y //= 2

    return ans


if __name__ == "__main__":
    m = int(input())
    mod = 1000000007
    arr = [list(map(int, input().split())) for _ in range(m)]
    arr2 = []
    ans = 0

    for n, s in arr:
        reverse_n = mul(n, mod-2, mod)
        q = (s * reverse_n) % mod
        ans += q
        ans %= mod
    print(ans)
