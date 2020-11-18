import sys
input = sys.stdin.readline

N = int(input())
arr = []
for i in range(N):
    arr.append(input().split())

for mid in range(N):
    for fr in range(N):
        for to in range(N):
            if arr[fr][mid] == '1' and arr[mid][to] =='1':
                arr[fr][to] = '1'

for i in range(N):
    print(' '.join(arr[i]))