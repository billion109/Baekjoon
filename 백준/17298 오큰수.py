n = int(input())
arr = list(map(int, input().split()))
stack = [[0, arr[0]]]
arr2 = [-1] * n
for i in range(1, n):
    curr = [i, arr[i]]
    while stack:
        last = stack.pop()
        if last[1] < curr[1]:
            arr2[last[0]] = curr[1]
        else:
            stack.append(last)
            break
    stack.append(curr)
print(*arr2)