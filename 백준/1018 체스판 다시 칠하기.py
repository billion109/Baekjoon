n,m = map(int, input().split())
arr=[]
for i in range(n):
    arr2= []
    str = input()
    for j in range(m):
        arr2.append(str[j])
    arr.append(arr2)

val = 0
chess = [['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
         ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
         ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
         ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
         ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
         ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
         ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
         ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']]


for i in range(n-7):
    for j in range(m-7):
        sum=0
        for k in range(8):
            for l in range(8):
                if chess[k][l] == arr[i+k][j+l]:
                    sum+=1
                else:
                    sum-=1
        if abs(sum)>=val:
            val=abs(sum)

answer = (64-val)/2
print(int(answer))


