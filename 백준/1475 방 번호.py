import sys
input = sys.stdin.readline

if __name__ == "__main__":
    arr = [0]*9
    str = str(input().rstrip())
    for i in str:
        t = int(i)
        if t==9:
            arr[6]+=1
        else:
            arr[t]+=1

    if arr[6] % 2 == 1:
        arr[6] = arr[6]//2 +1
    else:
        arr[6] = arr[6]//2

    print(max(arr))