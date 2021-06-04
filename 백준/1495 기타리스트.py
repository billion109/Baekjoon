import sys

input = sys.stdin.readline

if __name__ == "__main__":
    n, s, m = map(int, input().split())
    v = list(map(int, input().split()))
    dp = [set(s)]
    for i in range(n):
        tmp = []





"""
3 9 10
1 10 1

1 1 1
1
"""