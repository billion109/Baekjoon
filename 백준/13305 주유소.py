import sys

input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    roads = list(map(int, input().split()))
    costs = list(map(int, input().split()))
    ans = 0
    min_cost = costs[0]

    for i in range(n - 1):
        min_cost = min(min_cost, costs[i])
        ans += min_cost * roads[i]

    print(ans)
