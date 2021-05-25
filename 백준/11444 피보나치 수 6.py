import sys

input = sys.stdin.readline
val = 1000000007


def fun(arr1, arr2):
    x1, x2 = arr1[0]
    x3, x4 = arr1[1]

    y1, y2 = arr2[0]
    y3, y4 = arr2[1]

    arr_square = []
    arr_square.append([(x1 * y1 + y2 * x3) % val, (y1 * x2 + y2 * x4) % val])
    arr_square.append([(x1 * y3 + x3 * y4) % val, (x2 * y3 + y4 * x4) % val])
    return arr_square


if __name__ == "__main__":
    n = int(input())
    bin_n = bin(n)
    matrix_list = [[[1, 1], [1, 0]]]
    ans = [[1, 0], [0, 1]]
    for i in range(len(bin_n) - 3):
        matrix_list.append(fun(matrix_list[-1], matrix_list[-1]))

    for i in range(len(bin_n) - 2):
        if bin_n[len(bin_n) - i - 1] == '1':
            ans = fun(ans, matrix_list[i])

    print(ans[0][1])
