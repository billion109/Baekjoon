import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**8)
n = int(input().rstrip())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))
in_location=[0 for _ in range(n+1)]#인자를 찾을때 한번에 찾기위해서
for i in range(n):
    in_location[inorder[i]]=i

def fun(start, end, poststart, postend):
    #print([start, end, poststart, postend], inorder[start:end], postorder[poststart:postend])
    if poststart<=postend:

        center = postorder[postend]
        print(center, end=' ')
        temp = in_location[center]
        fun(start, temp-1, poststart, poststart+temp-start-1)
        fun(temp + 1, end, postend-end+temp, postend - 1)




fun(0, n-1, 0, n-1)

'''
15
8 4 9 2 10 5 11 1 12 6 13 3 14 7 15
8 9 4 10 11 5 2 12 13 6 14 15 7 3 1
'''
