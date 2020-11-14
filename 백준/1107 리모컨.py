import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
broken = list(map(int, input().split()))
not_broken = []
for i in range(10):
    if i in broken:
        continue
    not_broken.append(i)

cur = 100
ans = []
length = []
if N>=10:
    length.append(len(str(N))-1)
length.append(len(str(N)))
if N<100000:
    length.append(len(str(N))+1)

def move(cur, dst):
    return abs(cur-dst)

#1. 직접움직이기
ans.append(100)

#2. 최적을 찾기
for i in length:
    if i<len(str(N)):
        ans.append(int(str(max(not_broken))*i))
    elif i == len(str(N)):
        arr = []
        for num in str(N):
            lo = -1
            hi = 10
            for j in not_broken:
                if j>lo and j<=num:



    else:
        if not_broken[0]==0:
            temp = str(not_broken[1])
            temp+= '0'*(i-1)
            ans.append(int(temp))
        else:
            ans.append(int(str(min(not_broken))*i))


if M == 10:
    print(ans[0])
else:
    pass

print(ans)

ans = [move(x,N) for x in ans]
print(ans)
