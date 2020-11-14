import math
a, b, v = map(int, input().split())
sum = 0
total = 0

if v== a:
    print(1)
else:
    total = v-a
    num = total/(a-b)
    if total%(a-b) == 0:
        print(int(num)+1)
    else:
        print(int(math.floor(num))+2)