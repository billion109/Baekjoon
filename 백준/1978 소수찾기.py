n = int(input())
val = list(map(int, input().split()))
sum = 0
num = max(val)
a = [False,False]+[True]*(num-1)
primes = []

for i in range(2, num+1):
    if a[i]:
        primes.append(i)
        for j in range(2*i, num+1, i):
            a[j] = False

for i  in val:
    if i in primes:
        sum+=1
print(sum)