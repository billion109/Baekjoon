n =int(input())
arr=[]
for i in range(n):
    arr. append(input().split())
    arr[i].append(i)
    arr[i][0] = int(arr[i][0])
arr = sorted(arr, key=lambda x: (x[0], x[2]))
for i in range(n):
    print(arr[i][0],arr[i][1])