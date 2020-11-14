sum = 0
num = int(input())
for i in range(num):
    x = input()
    arr = []
    check = 1
    temp = 'null'
    for j in x:
        if j in arr:
            if j !=temp:
                check = 0
                break
        arr.append(j)
        temp = j
    if check == 1:
        sum+=1
print(sum)

