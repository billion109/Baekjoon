n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int,input().split())))

def last(n):
    return n[1]
def first(n):
    return n[0]
arr = sorted(arr, key=lambda x : (x[1],x[0]))
for _ in range(n):
    print(arr[_][0],arr[_][1])