import sys
n = int(input())

arr = [0]*10000
for i in range(n):
    num = int(sys.stdin.readline())
    arr[num-1]+=1

for i in range(10000):
    for j in range(arr[i]):
        print(i+1)



