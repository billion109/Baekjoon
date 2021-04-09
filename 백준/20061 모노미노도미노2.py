import sys

input = sys.stdin.readline


def convert(block, color):
    t, x, y = block
    if color == 'g':
        # t==1 -> x,y
        # t==2 -> 오른쪽으로 한개더
        # t==2 -> 아래로 한개더
        if t == 1:
            return [t, [x, y]]
        elif t == 2:
            return [t, [x, y], [x, y + 1]]
        else:
            return [t, [x, y], [x + 1, y]]

    if color == 'b':
        # green을 transpose
        if t == 1:
            return [t, [y, x]]
        elif t == 2:
            return [t, [y, x], [y + 1, x]]
        else:
            return [t, [y, x], [y, x + 1]]


def stack_block(block, color):
    t = block[0]
    pos_y = block[1][1]
    pos_x = 0
    global score

    if t == 1:
        while True:
            if pos_x + 1 <= 5 and arr[color][pos_x + 1][pos_y] == False:
                pos_x += 1
                continue
            break
        arr[color][pos_x][pos_y] = True

    elif t == 2:
        if color == 0:

            while True:
                if pos_x + 1 <= 5 and arr[color][pos_x + 1][pos_y] == False and arr[color][pos_x + 1][pos_y + 1] == False:
                    pos_x += 1
                    continue
                break

            arr[color][pos_x][pos_y] = True
            arr[color][pos_x][pos_y + 1] = True

        if color == 1:
            pos_x = 1
            pos_y = block[2][1]
            while True:
                if pos_x + 1 <= 5 and arr[color][pos_x + 1][pos_y] == False:
                    pos_x += 1
                    continue
                break
            arr[color][pos_x][pos_y] = True
            arr[color][pos_x-1][pos_y] = True
    else:
        if color == 0:
            pos_x = 1
            while True:
                if pos_x + 1 <= 5 and arr[color][pos_x + 1][pos_y] == False:
                    pos_x += 1
                    continue
                break
            arr[color][pos_x][pos_y] = True
            arr[color][pos_x - 1][pos_y] = True
        if color ==1:
            pos_x = 0
            pos_y = block[1][1]
            while True:
                if pos_x + 1 <= 5 and arr[color][pos_x + 1][pos_y] == False and arr[color][pos_x + 1][pos_y + 1] == False:
                    pos_x += 1
                    continue
                break
            arr[color][pos_x][pos_y] = True
            arr[color][pos_x][pos_y + 1] = True
    index = 5
    while index > 1:
        if arr[color][index][0] and arr[color][index][1] and arr[color][index][2] and arr[color][index][3]:
            score += 1
            for i in range(index, 0, -1):
                arr[color][i] = arr[color][i - 1][:]
            continue
        index -= 1
    if arr[color][0][0] or arr[color][0][1] or arr[color][0][2] or arr[color][0][3]:
        for i in range(5, 1, -1):
            arr[color][i] = arr[color][i - 2][:]
        arr[color][0] = [False] * 4
        arr[color][1] = [False] * 4
    elif arr[color][1][0] or arr[color][1][1] or arr[color][1][2] or arr[color][1][3]:
        for i in range(5, 1, -1):
            arr[color][i] = arr[color][i - 1][:]
        arr[color][1] = [False] * 4


if __name__ == "__main__":
    n = int(input())
    score = 0
    cnt = 0
    arr = [[[False] * 4 for _ in range(6)], [[False] * 4 for _ in range(6)]]
    # 1번째는 green 2번째는 blue0
    for _ in range(n):
        red_block = list(map(int, input().split()))
        green_block = convert(red_block, 'g')
        blue_block = convert(red_block, 'b')
        stack_block(green_block, 0)
        stack_block(blue_block, 1)

        # print(str(_) + "번째")
        # print('green')
        # for i in range(6):
        #     for j in range(4):
        #         print(arr[0][i][j],end=' ')
        #     print()
        # print()
        # print('blue')
        # for i in range(6):
        #     for j in range(4):
        #         print(arr[1][i][j],end=' ')
        #     print()



for i in range(4):
    for j in range(4):
        if arr[0][i + 2][j]:
            cnt += 1
        if arr[1][i + 2][j]:
            cnt += 1
print(score)
print(cnt)
