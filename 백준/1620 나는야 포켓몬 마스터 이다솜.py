import sys
from collections import deque
input = sys.stdin.readline

N,M = map(int, input().split())
arr = []
for i in range(N):
    arr.append(input().rstrip())

for i in range(M):
    t = input().rstrip()
    if t.isdigit():
        print(arr[int(t)-1])
    else:
        print(arr.index(t)+1)