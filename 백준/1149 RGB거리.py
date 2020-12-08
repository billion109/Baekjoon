import sys
input = sys.stdin.readline

N = int(input())
house = [list(map(int,input().split())) for _ in range(N)]

dp_R = [house[0][0]]
dp_G = [house[0][1]]
dp_B = [house[0][2]]

for i in range(1,N):
    dp_R.append(min(dp_G[i - 1], dp_B[i - 1]) + house[i][0])
    dp_G.append(min(dp_R[i - 1], dp_B[i - 1]) + house[i][1])
    dp_B.append(min(dp_G[i - 1], dp_R[i - 1]) + house[i][2])

print(min(dp_R[-1],dp_G[-1],dp_B[-1]))