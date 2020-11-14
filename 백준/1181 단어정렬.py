n = int(input())
arr = []



for _ in range(n):
    arr.append(input())
arr = list(set(arr))
arr = sorted(arr, key = lambda x:(len(x),x))

for _ in range(len(arr)):
    print(arr[_])