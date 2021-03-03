from collections import defaultdict


def fun(x):
    temp = []
    a = x[0]
    b = x[1]

    if a == '9':
        if b == '0':
            temp.append('80')
            temp.append('91')
        elif b == '9':
            temp.append('89')
            temp.append('98')
        else:
            temp.append('8' + b)
            temp.append('9' + str(int(b) + 1))
            temp.append('9' + str(int(b) - 1))
    else:
        if b == '0':
            temp.append(str(int(a) + 1) + '0')
            if a != '1':
                temp.append(str(int(a) - 1) + '0')
            temp.append(a + '1')
        elif b == '9':
            temp.append(str(int(a) + 1) + '9')
            if a != '1':
                temp.append(str(int(a) - 1) + '9')
            temp.append(a + '8')
        else:
            temp.append(str(int(a) + 1) + b)
            if a != '1':
                temp.append(str(int(a) - 1) + b)
            temp.append(a + str(int(b) + 1))
            temp.append(a + str(int(b) - 1))

    return temp


n = int(input())
arr = [{'90': 1}]
ans = [1]

for i in range(n - 10):
    prev = arr[i]
    temp = defaultdict(int)
    temp_val = 0
    for k, v in prev.items():
        temp_list = fun(k)
        for j in temp_list:
            temp[j] += v
            temp_val += v
    arr.append(temp)
    ans.append(temp_val)

print(arr)
print(ans)
print(sum(ans))

aawe = ['90', '99', '88', '11', '10','99','19','18']
for i in aawe:
    print(i + ':' , fun(i))
