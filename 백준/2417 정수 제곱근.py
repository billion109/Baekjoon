import sys
from bisect import bisect_left

input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    left = 0
    right = n
    while left <= right:
        mid = (left + right) // 2
        val = mid ** 2
        if val == n:
            break
        elif val > n:
            right = mid - 1
        else:
            left = mid + 1
    if left>right:
        mid = left
    print(mid)
