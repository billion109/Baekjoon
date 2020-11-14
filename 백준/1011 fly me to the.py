import math
num = int(input())
arr = []
for i in range(num):
    x,y = map(int, input().split())
    range_xy = y-x
    if range_xy ==1:
        arr.append(1)
        continue
    sq_ran = math.sqrt(range_xy)
    fl_sq_ran = math.floor(float(sq_ran))
    if sq_ran==fl_sq_ran:
        arr.append(fl_sq_ran*2-1)
        continue
    sum = fl_sq_ran*2
    if range_xy <= fl_sq_ran**2+fl_sq_ran:
        arr.append(sum)
    else:
        arr.append(sum+1)

for i in arr:
    print(i)
