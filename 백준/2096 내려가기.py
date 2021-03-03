import sys

input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    arr = []
    for i in range(n):
        a, b, c = map(int, input().split())
        if i == 0:
            dp1, dp2, dp3, dp4, dp5, dp6 = a, b, c, a, b, c
        else:
            temp1 = max(dp1, dp2) + a
            temp2 = max(dp1, dp2, dp3) + b
            temp3 = max(dp2, dp3) + c
            dp1, dp2, dp3 = temp1, temp2, temp3

            temp4 = min(dp4, dp5) + a
            temp5 = min(dp4, dp5, dp6) + b
            temp6 = min(dp5, dp6) + c
            dp4, dp5, dp6 = temp4, temp5, temp6

    max_val = max(dp1, dp2, dp3)
    min_val = min(dp4, dp5, dp6)

    print(max_val, min_val)
