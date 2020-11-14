n = int(input())

arr = [1,2]
for i in range(n):
    arr.append((arr[i]+arr[i+1])%15746)

print(arr[n-1])

