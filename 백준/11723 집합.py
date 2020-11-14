import sys
input = sys.stdin.readline

S = [0 for i in range(20)]
M = int(input())
for i in range(M):
    t = input().split()
    if t[0] == 'add':
        S[int(t[1])-1]=1
    if t[0] == 'check':
        if S[int(t[1])-1] == 1:
            print(1)
        else:
            print(0)
    if t[0] == 'remove':
        S[int(t[1])-1]=0
    if t[0] == 'toggle':
        if S[int(t[1])-1] == 1:
            S[int(t[1])-1] = 0
        else:
            S[int(t[1])-1] = 1
    if t[0] == 'all':
        S = [1 for i in range(20)]
    if t[0] == 'empty':
        S = [0 for i in range(20)]
