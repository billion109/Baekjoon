n = int(input())
arr = [['-']*n for x in range(n)]
k = int(input())

for _ in range(k):
    n,m = map(int,input().split())
    arr[n-1][m-1] = 'A'

L = int(input())
direction = list(input().split())

