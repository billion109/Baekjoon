def check(arr,x,y,n):
    blue = 0
    for i in range(n):
        for j in range(n):
            if arr[x+i][y+j] =='1':
                blue+=1
    return blue

def square(arr,bb,x,y,n):
    p = check(arr,x,y,n)
    if p== n**2:
        bb[1]+=1
        return
    elif p == 0:
        bb[0]+=1
        return
    else:
        square(arr,bb,x,y,int(n/2))
        square(arr, bb,int(x+n/2), y, int(n / 2))
        square(arr,bb, x, int(y+n/2), int(n / 2))
        square(arr,bb, int(x+n/2), int(y+n/2), int(n / 2))
        return
n = int(input())
arr= []
bb = [0,0]
for _ in range(n):
    arr.append(list(input().split()))

val = square(arr,bb,0,0,n)
print(bb[0])
print(bb[1])