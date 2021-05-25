import sys
import math

input = sys.stdin.readline

if __name__ == "__main__":
    n, m = map(int, input().split())
    ans = math.comb(n, 3)
    comb_set = set()
    for i in range(m):
        x, y = map(int, input().split())
        for j in range(1, n + 1):
            if j == x or j == y:
                continue
            temp = [x, y, j]
            temp.sort()
            temp = list(map(str, temp))
            temp = ".".join(temp)
            comb_set.add(temp)

    # print(comb_set)
    print(ans - len(comb_set))
