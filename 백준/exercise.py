arr = [[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]]

print(*arr)
print(list(zip(*arr)))
arr = list(map(list, zip(*arr)))

for i in arr:
    print(*i)
