import sys

input = sys.stdin.readline
N, M = map(int,input().split())
arr = list(map(int, input().split()))


def sum_tree(h):
    temp = 0
    for i in arr:
        if i>h:
            temp+=(i-h)
    return temp

def bn_search(low, high):
    if low>high:
        return -1
    mid = (low+high)//2
    t = sum_tree(mid)
    #print(low,mid,high, sum_tree(mid))

    if t < M:
        return bn_search(low, mid-1)
    elif t > M:
        temp2 = bn_search(mid+1, high)
        if temp2 == -1:
            return mid
        else:
            return temp2
    else:
        return mid

print(bn_search(0, max(arr)))

