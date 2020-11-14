import sys
input = sys.stdin.readline
N, M = map(int, input().split())
dic = {}
for i in range(N):
    a,b = input().split()
    dic[a] = b
for i in range(M):
    print(dic[input().rstrip()])