import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
for i in range(n):
    m = int(input())
    dic = defaultdict(list)
    for j in range(m):
        x,y = input().split()
        dic[y].append(x)
    ans = 1
    for j in dic.keys():
        ans*=(len(dic[j])+1)
    print(ans-1)