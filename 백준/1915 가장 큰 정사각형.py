import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n, m = map(int, input().split())
    board = [list(map(int,list(input().rstrip()))) for _ in range(n)]
    dp = [[0] * m for _ in range(n)]
    ans = 0

    for i in range(n):
        for j in range(m):
            if board[i][j] == 1:
                try:
                    dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1], dp[i][j - 1]) + 1
                except IndexError:
                    dp[i][j] = 1

            ans = max(dp[i][j], ans)
    print(ans**2)

"""
5 5
01000
01110
01110
11111
11011

4 4
0100
0111
1111
0011

4 4
0100
0111
1111
1110

4 4
1111
0111
1110
0010

4 4
1111
1111
1111
1111

4 4
0000
0000
0000
0000

4 4
1111
1111
0000
0000

4 4
1010
0101
1010
0101

5 5
11111
11111
11011
11111
11111
"""
