n = int(input())
i = 2
while True:
    if n%i==0:
        print(i)
        n/=i
    else:
        if i>=n:
            if n!=1:
                print(n)
                break
            break
        i+=1
