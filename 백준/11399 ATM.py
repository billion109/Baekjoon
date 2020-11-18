import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int,input().split()))
arr.sort()

sum = 0
for i in range(N):
    sum+=(N-i)*arr[i]

print(sum)
