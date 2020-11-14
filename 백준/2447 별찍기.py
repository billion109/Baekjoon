def star(x, y, n):
    for i in range(int(x+n), int(x+2*n)):
        for j in range(int(y+n), int(y+2*n)):
            arr[i][j]= ' '
    if n!=1:
        star(x,y,n/3)
        star(x+n,y,n/3)
        star(x+2*n, y, n / 3)
        star(x, y+n, n / 3)
        star(x+2*n, y+n, n / 3)
        star(x, y+2*n, n / 3)
        star(x+n, y+2*n, n / 3)
        star(x+2*n, y+2*n, n / 3)

def show():
    for i in range(len(arr)):
        for j in range(len(arr)):
            print(arr[i][j], end='')
        print()

n = int(input())
arr = [['*']*n for _ in range(n)]
star(0,0,n/3)
show()
