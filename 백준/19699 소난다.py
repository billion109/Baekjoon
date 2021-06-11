from itertools import combinations

n, m = map(int, input().split())
h = list(map(int, input().split()))
che = [False, False] + [True] * 5000
prime = []

for i in range(2, sum(h)+1):
    if che[i]:
        prime.append(i)
        for j in range(2*i, sum(h)+1, i):
            che[j] = False

ans = set()
for i in combinations(h, m):
    if sum(i) in prime:
        ans.add(sum(i))

if len(ans) == 0:
    print(-1)
else:
    ans = list(ans)
    ans.sort()
    print(*ans)


