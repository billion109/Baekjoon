n = int(input())
arr = [0,1]
for i in range(40):
    arr.append(arr[i]+arr[i+1])

for _ in range(n):
    v = int(input())
    if v==0:
        print(1,0)
    else:
        print(arr[v-1],arr[v])