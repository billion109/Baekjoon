import sys

input = sys.stdin.readline


# R : 한 칸 오른쪽으로
# L : 한 칸 왼쪽으로
# B : 한 칸 아래로
# T : 한 칸 위로
# RT : 오른쪽 위 대각선으로
# LT : 왼쪽 위 대각선으로
# RB : 오른쪽 아래 대각선으로
# LB : 왼쪽 아래 대각선으로

def pos(string):
    col = ord(string[0]) - 65
    row = int(string[1]) - 1
    return row, col


def pos_reverse(row, col):
    row = str(row + 1)
    col = chr(col + 65)
    return col + row


if __name__ == "__main__":
    board = [[0] * 8 for _ in range(8)]
    k, s, n = input().split()
    for i in range(int(n)):
        cmd = input().rstrip()
        curr_r, curr_c = pos(k)
        next_r, next_c = curr_r, curr_c
        if cmd == "R":
            next_c = curr_c + 1
        elif cmd == "L":
            next_c = curr_c - 1
        elif cmd == "B":
            next_r = curr_r - 1
        elif cmd == "T":
            next_r = curr_r + 1
        elif cmd == "RT":
            next_c = curr_c + 1
            next_r = curr_r + 1
        elif cmd == "LT":
            next_c = curr_c - 1
            next_r = curr_r + 1
        elif cmd == "RB":
            next_c = curr_c + 1
            next_r = curr_r - 1
        elif cmd == "LB":
            next_c = curr_c - 1
            next_r = curr_r - 1

        curr_stone_r, curr_stone_c = pos(s)
        if curr_stone_r == next_r and curr_stone_c == next_c:
            next_stone_c = curr_stone_c + (next_c - curr_c)
            next_stone_r = curr_stone_r + (next_r - curr_r)
        else:
            next_stone_c = curr_stone_c
            next_stone_r = curr_stone_r

        # print(next_r,curr_r,next_c,curr_c,next_stone_r,curr_stone_r,next_stone_c,curr_stone_c)

        if 0 <= next_c < 8 and 0 <= next_r < 8 and 0 <= next_stone_c < 8 and 0 <= next_stone_r < 8:
            k = pos_reverse(next_r, next_c)
            s = pos_reverse(next_stone_r, next_stone_c)
        # print(k,s)

    print(k)
    print(s)