n = int(input())

fib = [1,2]

if n == 1:
    print(1)
elif n == 2:
    print(2)
else:
    for i in range(2,n):
        fib.append(fib[i-2]+fib[i-1])
    print(fib[n-1]%10007)