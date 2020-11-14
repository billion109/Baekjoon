import sys
input = sys.stdin.readline

K,N = map(int,input().split())
arr = []
for i in range(K):
    arr.append(int(input()))

lo = 1
hi = max(arr)
ans = 0

def lan_cnt(val):
    temp = 0
    for i in arr:
        temp+=(i//val)
    return temp

while lo<=hi:
    mid = (lo+hi)//2
    t = lan_cnt(mid)

    #print(lo,mid,hi,t,ans)
    if t>=N:
        ans = mid
        lo = mid+1

    else:
        hi = mid-1

print(ans)
