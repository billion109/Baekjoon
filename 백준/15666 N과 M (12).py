import sys
input = sys.stdin.readline

N, M = map(int,input().split())
num = list(map(int,input().split()))
num = list(set(num))
num.sort()

def fun(arr, count, box):
    for i in range(len(arr)):
        temp = arr[i:]
        temp2 = box[:]
        temp2.append(arr[i])
        if count < M:
            fun(temp, count+1, temp2)
        else:
            for val in temp2:
                print(val, end= ' ')
            print()


fun(num, 1, [])
