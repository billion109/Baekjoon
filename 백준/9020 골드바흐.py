import sys

num = int(input())
a = [False,False]+[True]*(9999)
primes = []

for i in range(2, 10001):
    if a[i]:
        primes.append(i)
        for j in range(2*i, 10001, i):
            a[j] = False

for _ in range(num):
    i = int(sys.stdin.readline().rstrip())
    for j in range(i//2,1,-1):
        if j in primes and i-j in primes:
            print(j, i-j)
            break

