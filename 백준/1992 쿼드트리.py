import sys
input = sys.stdin.readline

N = int(input())
arr =  []
for i in range(N):
    arr.append(list(map(int,list(input().rstrip()))))


def fun(i,j,n):
    if n == 1:
        if arr[i][j]==1:
            print(1,end='')
        else:
            print(0,end='')
    else:
        temp = 0
        for x in range(i,i+n):
            for y in range(j,j+n):
                temp+=arr[x][y]
        if temp ==0:
            print(0,end='')
        elif temp == n**2:
            print(1,end='')
        else:
            new_n = n//2
            print('(',end='')
            fun(i,j,new_n)
            fun(i,j+new_n,new_n)
            fun(i+new_n,j,new_n)
            fun(i+new_n,j+new_n,new_n)
            print(')',end='')



fun(0,0,N)

