import sys

input = sys.stdin.readline

if __name__ == "__main__":
    d, k = map(int, input().split())
    arr = [[1, 0], [0, 1]]
    for i in range(2, d):
        x = arr[i - 2][0] + arr[i - 1][0]
        y = arr[i - 2][1] + arr[i - 1][1]
        arr.append([x, y])

    x, y = arr[d - 1][0], arr[d - 1][1]
    ans_x, ans_y = 0,0
    for i in range(k):
        if (k - i * x) % y == 0:
            ans_x = i
            ans_y = (k - i * x) // y
            break

    print(ans_x)
    print(ans_y)
