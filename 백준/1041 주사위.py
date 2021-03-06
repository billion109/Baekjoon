import sys
from itertools import combinations

input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    dice = list(map(int, input().split()))

    # 2면의 최솟값구하기
    temp = [sum(i) for i in (list(combinations(dice, 2)))]
    temp2 = [dice[0] + dice[5], dice[1] + dice[4], dice[3] + dice[2]]
    for i in temp2:
        temp.remove(i)
    two_min = min(temp)

    # 3면의 최솟값
    temp = [[0,1,2],[0,1,3],[0,4,2],[0,4,3],[5,1,2],[5,1,3],[5,4,2],[5,4,3]]
    temp2 = []
    for a,b,c in temp:
        temp2.append(dice[a]+dice[b]+dice[c])
    three_min = min(temp2)

    if n == 1:
        print(sum(dice) - max(dice))
    elif n == 2:
        print(two_min * 4 + three_min * 4)
    else:
        ans = 0
        ans += 4 * three_min
        ans += 4 * two_min
        ans += (n - 2) * 4 * min(dice)
        ans += (n - 2) * 8 * two_min
        ans += ((n - 2) ** 2) * 5 * min(dice)
        print(ans)
