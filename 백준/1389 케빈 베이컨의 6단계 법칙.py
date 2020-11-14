import sys
from collections import defaultdict
input = sys.stdin.readline
dic = defaultdict(list)
max_val = float('inf')

N, M = map(int,input().split())
arr = [[max_val for x in range(N)] for y in range(N)]

for i in range(M):
    fr,to = map(int,input().split())
    dic[fr].append(to)
    dic[to].append(fr)

for i in range(N):
    arr[i][i]=0

for key, values in dic.items():
    for v in values:
        arr[key-1][v-1] = 1

for m in range(N):
    for s in range(N):
        for e in range(N):
            if s!=e:
                arr[s][e] = min(arr[s][e], arr[s][m]+arr[m][e])

ans = [sum(x) for x in arr]
print(ans.index(min(ans))+1)




