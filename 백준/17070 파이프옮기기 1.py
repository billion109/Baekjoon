from collections import deque, defaultdict
import sys

input = sys.stdin.readline


def solution(n, house):
    horizontal = 0
    vertical = 1
    diagonal = 2
    dp = [[[0] * n for _ in range(n)] for _ in range(3)]

    pipe_dict = defaultdict(list)
    pipe_dict["1"].append([0, 1, horizontal])
    dp[horizontal][0][1] = 1

    # dp를 처리하기위해 거리순(x+y값의 합)으로 계산
    for i in range(2 * n):
        # 딕셔너리안에 중복되는값 제거
        if pipe_dict[str(i)]:
            pipe_dict[str(i)] = list(set([tuple(item) for item in pipe_dict[str(i)]]))

        while pipe_dict[str(i)]:
            row, col, position = pipe_dict[str(i)].pop()
            if position == horizontal:
                if 0 <= col + 1 < n and house[row][col + 1] == 0:
                    pipe_dict[str(row + col + 1)].append([row, col + 1, horizontal])
                    dp[horizontal][row][col + 1] += dp[horizontal][row][col]

                    if 0 <= row + 1 < n and house[row + 1][col + 1] == 0 and house[row + 1][col] == 0:
                        pipe_dict[str(row + col + 2)].append([row + 1, col + 1, diagonal])
                        dp[diagonal][row + 1][col + 1] += dp[horizontal][row][col]

            elif position == vertical:
                if 0 <= row + 1 < n and house[row + 1][col] == 0:
                    pipe_dict[str(row + col + 1)].append([row + 1, col, vertical])
                    dp[vertical][row + 1][col] += dp[vertical][row][col]

                    if 0 <= col + 1 < n and house[row + 1][col + 1] == 0 and house[row][col + 1] == 0:
                        pipe_dict[str(row + col + 2)].append([row + 1, col + 1, diagonal])
                        dp[diagonal][row + 1][col + 1] += dp[vertical][row][col]

            elif position == diagonal:
                if 0 <= row + 1 < n and 0 <= col + 1 < n and house[row + 1][col] == 0 and house[row][col + 1] == 0 and \
                        house[row + 1][col + 1] == 0:
                    pipe_dict[str(row + col + 2)].append([row + 1, col + 1, diagonal])
                    dp[diagonal][row + 1][col + 1] += dp[diagonal][row][col]

                if 0 <= col + 1 < n and house[row][col + 1] == 0:
                    pipe_dict[str(row + col + 1)].append([row, col + 1, horizontal])
                    dp[horizontal][row][col + 1] += dp[diagonal][row][col]

                if 0 <= row + 1 < n and house[row + 1][col] == 0:
                    pipe_dict[str(row + col + 1)].append([row + 1, col, vertical])
                    dp[vertical][row + 1][col] += dp[diagonal][row][col]

        # print(i + 1)
        # for x in range(n):
        #     for j in range(3):
        #         print(*dp[j][x], end='')
        #         print('   ', end='')
        #     print()
        # print('-------------')

    ans = 0
    for i in range(3):
        ans += dp[i][-1][-1]
    print(ans)


if __name__ == "__main__":
    n = int(input())
    house = [list(map(int, input().split())) for _ in range(n)]
    solution(n, house)
