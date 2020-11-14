def hanoi(n, fr, to):
    if n ==1:
        print(fr,to)
    else:
        if fr+to==3:
            x = 3
        elif fr+to==4:
            x= 2
        elif fr + to == 5:
            x = 1
        hanoi(n-1,fr,x)
        print(fr,to)
        hanoi(n-1,x,to)

n=int(input())
arr=[1]
for i in range(n):
    arr.append(arr[i]*2+1)
print(arr[n-1])
hanoi(n,1,3)
