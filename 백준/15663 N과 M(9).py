import sys

input = sys.stdin.readline

N, M = map(int, input().split())
num = list(map(int, input().split()))
num.sort()
ans = []


def fun(arr, count, box):
    global ans
    for i in range(len(arr)):
        temp = arr[:i] + arr[i + 1:]
        temp2 = box[:]
        temp2.append(arr[i])
        if count < M:
            fun(temp, count + 1, temp2)
        else:
            ans.append(temp2)


fun(num, 1, [])
ans.sort()
for i in range(len(ans)):
    if i == 0:
        for j in ans[i]:
            print(j, end=' ')
        print()
    else:
        if ans[i-1]!=ans[i]:
            for j in ans[i]:
                print(j, end=' ')
            print()