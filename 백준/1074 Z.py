import sys
input = sys.stdin.readline

N, r, c = map(int, input().split())
cnt = -1

def Z(n,r, c):
    global cnt
    #print(cnt, n, i, j)
    if n==1:
        if r==0 and c == 0:
            cnt+=1
        if r==0 and c ==1:
            cnt+=2
        if r==1 and c==0:
            cnt+=3
        if r==1 and c==1:
            cnt+=4
    else:
        dis = 2**(n-1)
        area = dis**2
        if r+1<=dis and c+1 <=dis:
            Z(n-1, r, c)
        if r+1<=dis and c+1 >dis:
            cnt+=area
            Z(n - 1, r, c-dis)
        if r+1>dis and c+1 <=dis:
            cnt+=2*area
            Z(n - 1, r-dis, c)
        if r+1>dis and c+1 >dis:
            cnt+=3*area
            Z(n - 1, r-dis, c-dis)


Z(N,r,c)
print(cnt)