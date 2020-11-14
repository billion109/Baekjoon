import sys
from _collections import defaultdict

n = int(input())
y = list(map(int, sys.stdin.readline().rstrip().split(' ')))
x = y[:]
x = list(set(x))
x.sort()
dic = defaultdict(int)
for i in range(len(x)):
    dic[x[i]] = i
for i in y:
    print(dic[i],end=' ')