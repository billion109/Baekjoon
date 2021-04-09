import sys
from collections import defaultdict

input = sys.stdin.readline


def next_index(r, c):
    new_r = r + dest[d][0] * s
    new_c = c + dest[d][1] * s
    while new_r < 0:
        new_r += N
    while new_c < 0:
        new_c += N

    new_r = new_r%N
    new_c = new_c%N

    if new_r ==0:
        new_r = N
    if new_c == 0:
        new_c = N
    return new_r, new_c


if __name__ == "__main__":
    N, M, K = map(int, input().split())
    fireball_dict = defaultdict(list)
    dest = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]

    for i in range(M):
        r, c, m, s, d = map(int, input().split())
        fireball_dict[str(r) + ',' + str(c)].append([m, s, d])

    for _ in range(K):
        new_fireball_dict = defaultdict(list)
        for index in fireball_dict.keys():
            for m, s, d in fireball_dict[index]:
                r, c = map(int, index.split(','))
                new_r, new_c = next_index(r, c)
                new_fireball_dict[str(new_r) + ',' + str(new_c)].append([m, s, d])

        fireball_dict = defaultdict(list)
        for index in new_fireball_dict.keys():
            cnt = len(new_fireball_dict[index])
            if cnt > 1:
                new_m, new_s = 0,0
                new_d = ''
                for m, s, d in new_fireball_dict[index]:
                    new_m += m
                    new_s += s
                    new_d += str(d % 2)

                new_m = new_m // 5
                if new_m == 0:
                    continue

                new_s = new_s // cnt
                if new_d == '0' * cnt or new_d == '1' * cnt:
                    new_d = [0, 2, 4, 6]
                else:
                    new_d = [1, 3, 5, 7]

                for _ in range(4):
                    fireball_dict[index].append([new_m, new_s, new_d[_]])
            else:
                fireball_dict[index].append(new_fireball_dict[index][0])

    ans = 0
    for index in fireball_dict.keys():
        for val in fireball_dict[index]:
            ans+=val[0]
    print(ans)