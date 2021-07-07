def ex_product(c, a, b):
    x = [c[0] - a[0], c[1] - a[1]]
    y = [c[0] - b[0], c[1] - b[1]]
    return 0.5 * (x[0] * y[1] - x[1] * y[0])


n = int(input())
arr = []
ans = 0
for i in range(n):
    arr.append(list(map(int, input().split())))

center = arr[0]
for i in range(1, n - 1):
    pos_a = arr[i]
    pos_b = arr[i + 1]
    ex_product_val = ex_product(center, pos_a, pos_b)
    ans+=ex_product_val

print(round(abs(ans),1))

