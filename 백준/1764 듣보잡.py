import sys
input = sys.stdin.readline
from collections import defaultdict

N, M = map(int, input().split())
dic = defaultdict(int)
arr = []
for i in range(N):
    dic[input().rstrip()]+=1

for i in range(M):
    t = input().rstrip()
    if dic[t]==1:
        arr.append(t)

arr.sort()
print(len(arr))
print("\n".join(arr))
