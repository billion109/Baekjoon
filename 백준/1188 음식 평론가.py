import sys

input = sys.stdin.readline
ans = 0


def fun(bread, people):
    ans = 0
    if bread >= people:
        bread = bread % people

    if bread == 0:
        return 0

    if people % bread == 0:
        return ((people // bread) - 1) * bread
    else:
        ans += (people // bread) * bread
        ans += fun(bread, people - (people // bread) * bread)
        return ans


n, m = map(int, input().split())
ans = fun(n, m)
print(ans)
