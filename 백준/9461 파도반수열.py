n = int(input())
arr = [1,1,1,2,2]
for i in range(95):
    arr.append(arr[i]+arr[i+4])

for _ in range(n):
    print(arr[int(input())-1])