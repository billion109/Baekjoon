m = int(input())
n = int(input())

a = [False,False]+[True]*(n-1)
primes = []

for i in range(2, n+1):
    if a[i]:
        if i>=m:
            primes.append(i)
        for j in range(2*i, n+1, i):
            a[j] = False

sum = 0
if len(primes) == 0:
    print(-1)
else:
    for i in primes:
        sum +=i
    print(sum)
    print(primes[0])