arr=[]

while True:
    n = int(input())
    if n == 0:
        break

    a = [False, False] + [True] * (2*n - 1)
    primes = []

    for i in range(2, 2*n+1):
        if a[i]:
            if i>n:
                primes.append(i)
            for j in range(2*i, 2*n+1, i):
                a[j] = False

    arr.append(len(primes))

for i in arr:
    print(i)
