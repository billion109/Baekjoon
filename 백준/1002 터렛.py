import math
num = int(input())
for _ in range(num):
    x1,y1,r1,x2,y2,r2 = map(int, input().split())
    length = math.sqrt((x1-x2)**2+(y1-y2)**2)
    r_length = r1+r2
    r_length2 = abs(r1-r2)

    if r1 == r2 and x1 == x2 and y1 == y2:
        print(-1)
    else:
        if length > max(r1,r2):
            if length > r_length:
                print(0)
            if length < r_length:
                print(2)
            if length == r_length:
                print(1)
        elif length <max(r1,r2):
            if length > r_length2:
                print(2)
            if length < r_length2:
                print(0)
            if length == r_length2:
                print(1)
        else:
            print(2)



