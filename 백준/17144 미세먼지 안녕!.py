import sys

input = sys.stdin.readline

if __name__ == "__main__":
    room = []
    air_cleaner = []
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    r, c, t = map(int, input().split())
    for i in range(r):
        temp = list(map(int, input().split()))
        if temp[0] == -1:
            air_cleaner.append(i)
        room.append(temp)

    for _ in range(t):
        # 1. 미세먼지확산
        temp = [[0] * c for _ in range(r)]
        temp[air_cleaner[0]][0] = -1
        temp[air_cleaner[1]][0] = -1
        for i in range(r):
            for j in range(c):
                if room[i][j] == 0 or room[i][j] == -1:
                    continue
                val = room[i][j]
                new_val = val
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if 0 <= nx < r and 0 <= ny < c and room[nx][ny] != -1:
                        temp[nx][ny] += val // 5
                        new_val -= val // 5
                temp[i][j] += new_val
        room = temp[:][:]


        # 2. 공기청정기
        # 2-1 윗방향
        pos = air_cleaner[0]
        for i in reversed(range(pos)):
            if i == pos - 1:
                continue
            room[i + 1][0] = room[i][0]

        for i in range(c - 1):
            room[0][i] = room[0][i + 1]

        for i in range(pos):
            room[i][c - 1] = room[i + 1][c - 1]
        for i in reversed(range(c - 1)):
            if i == 0:
                room[pos][i + 1] = 0
                continue
            room[pos][i + 1] = room[pos][i]

        # 2-2 아랫방향
        pos = air_cleaner[1]
        for i in range(pos + 1, r - 1):
            room[i][0] = room[i + 1][0]
        for i in range(c - 1):
            room[r - 1][i] = room[r - 1][i + 1]
        for i in reversed(range(pos + 1, r)):
            room[i][c - 1] = room[i - 1][c - 1]
        for i in reversed(range(c - 1)):
            if i == 0:
                room[pos][i + 1] = 0
                continue
            room[pos][i + 1] = room[pos][i]
        """
        for i in range(r):
            for j in range(c):
                print(room[i][j],end=' ')
            print()
        print('----')
        """
    count = 0
    for i in range(r):
        count += sum(room[i])
    print(count+2)