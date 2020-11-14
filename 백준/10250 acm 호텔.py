import math
num = int(input())
arr = []
for i in range(num):
    h, w, n = map(int, input().split())
    x = int(math.ceil(n/h))
    y = n%h
    if y == 0:
        y = h
    sum = 100*y + x
    arr.append(sum)
for i in arr:
    print(i)
