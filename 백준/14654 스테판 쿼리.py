import sys

input = sys.stdin.readline
from collections import deque


def fun(x, y):
    win = [[2, 1], [3, 2], [1, 3]]
    draw = [[1, 1], [2, 2], [3, 3]]
    lose = [[1, 2], [2, 3], [3, 1]]
    if [x, y] in win:
        return 1
    elif [x, y] in draw:
        return 2
    elif [x, y] in lose:
        return 3
    else:
        return 0


if __name__ == "__main__":
    n = int(input())
    a = deque(list(map(int, input().split())))
    b = deque(list(map(int, input().split())))
    ans = 0
    temp = [1, 0]
    while a or b:
        x = a.popleft()
        y = b.popleft()
        val = fun(x, y)
        win_team, win_cnt = temp

        if val == 1:
            if win_team == 1:
                temp[1] += 1
            else:
                temp = [1, 1]
        elif val == 2:
            if win_team == 1:
                temp = [2, 1]
            else:
                temp = [1, 1]
        elif val == 3:
            if win_team == 1:
                temp = [2, 1]
            else:
                temp[1] += 1
        else:
            print('wrong coding')

        ans = max(ans, temp[1])
    print(ans)
