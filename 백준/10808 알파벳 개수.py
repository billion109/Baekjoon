import sys
input = sys.stdin.readline

if __name__ == "__main__":
    str = input().rstrip()
    arr = [0]*26
    for i in str:
        arr[ord(i)-97]+=1

    print(*arr)
