import sys
from collections import defaultdict

N, M, B = map(int,(input().split(' ')))
dic = defaultdict(int)

for i in range(N):
    for j in list(map(int,sys.stdin.readline().split())):
        dic[j]+=1

ans = [M*N*2*256,0]
t = list(dic.keys())

for std in range(min(t),max(t)+1):
    time = 0
    block = B
    for x in dic.keys():
        temp = (x-std)*dic[x]
        if x>std:
            time += temp*2
            block += temp
        elif x<std:
            time += -temp
            block -= -temp

    if block>=0 and std<=256:
        if time<ans[0]:
            ans[0] = time
            ans[1] = std
        elif time == ans[0] and ans[1]<std:
            ans[1] = std

print(ans[0], ans[1])
