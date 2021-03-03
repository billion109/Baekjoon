import sys

input = sys.stdin.readline


def matrix_square(arr1, arr2):
    length = len(arr)
    temp = [[0] * length for _ in range(length)]
    for i in range(length):
        for j in range(length):
            for k in range(length):
                temp[i][j] += arr1[i][k] * arr2[k][j]
                temp[i][j] %= 1000
    return temp


if __name__ == "__main__":
    N, B = map(int, input().split())
    B_num = str(bin(B))[2:]
    arr = []
    matrix_box = []
    for _ in range(N):
        arr.append(list(map(int, input().split())))

    for i in range(len(B_num)):
        if i == 0:
            matrix_box.append(arr)
            continue
        matrix_box.append(matrix_square(matrix_box[-1], matrix_box[-1]))

    ans = []
    for i in range(N):
        temp = []
        for j in range(N):
            if i == j:
                temp.append(1)
            else:
                temp.append(0)
        ans.append(temp)

    for i in range(len(B_num)):
        if B_num[len(B_num) - i - 1] == '1':
            ans = matrix_square(ans, matrix_box[i])

    for i in range(N):
        for j in range(N):
            print(ans[i][j], end=' ')
        print()
