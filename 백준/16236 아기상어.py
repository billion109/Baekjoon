import sys
from collections import deque, defaultdict

input = sys.stdin.readline

# 0 = 빈칸
# 9 = 아기상어
# 123456 = 물고기크기

n = int(input())
time = 0
size = 2
ate_count = 0
pos = []
board = []
dxy = [(-1, 0), (0, -1), (0, 1), (1, 0)]


def bfs():
    global pos
    global board
    global time

    check_board = [[True] * n for _ in range(n)]
    queue = deque([])
    board_dict = defaultdict(list)

    queue.append([pos[0], pos[1], 0])
    check_board[pos[0]][pos[1]] = False

    while len(queue) > 0:
        # print(queue)
        # print(check_board)
        # print('------')

        pos_x, pos_y, t = queue.popleft()
        if board[pos_x][pos_y] < size and board[pos_x][pos_y] != 0 and board[pos_x][pos_y] != 9:
            board_dict[t].append([pos_x, pos_y, t])

        if len(board_dict) > 1:
            temp = board_dict[list(board_dict.keys())[0]]
            temp.sort()
            # print(queue)
            # print(temp)
            board[pos[0]][pos[1]] = 0
            pos = [temp[0][0], temp[0][1]]
            board[pos[0]][pos[1]] = 9
            time += temp[0][2]
            return 1

        for dx, dy in dxy:
            nx = pos_x + dx
            ny = pos_y + dy
            if 0 <= nx < n and 0 <= ny < n and check_board[nx][ny] and board[nx][ny] <= size:
                queue.append([nx, ny, t + 1])
                check_board[nx][ny] = False

    if len(board_dict) == 1:
        temp = board_dict[list(board_dict.keys())[0]]
        temp.sort()
        board[pos[0]][pos[1]] = 0
        pos = [temp[0][0], temp[0][1]]
        board[pos[0]][pos[1]] = 9
        time += temp[0][2]
        return 1

    return 0


for i in range(n):
    board.append(list(map(int, input().split())))
    if 9 in board[-1]:
        pos.append(i)
        pos.append(board[-1].index(9))

while True:
    '''
    print('size=', size)
    print('time=', time)
    print('ate=', ate_count)
    
    for i in range(n):
        for j in range(n):
            print(board[i][j], end=' ')
        print('')
    print('--------')
    '''
    success = bfs()
    if success == 0:  # 실패
        break

    elif success == 1:  # 먹음
        ate_count += 1

    if ate_count == size:
        size += 1
        ate_count = 0

# print(time, size, ate_count)
print(time)
