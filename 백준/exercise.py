import sys
input = sys.stdin.readline
from collections import deque, defaultdict

print('hello')
check_board = [[False] * 3 for _ in range(3)]
print(check_board)
check_board[0][0] = True
print(check_board)

dic = defaultdict(list)
print(len(dic))
dic[1].append([3,3])
print(len(dic))
dic[1].append([3,1])
print(len(dic))
dic[2].append([4,4])
print(len(dic))
print(dic)
print(dic.keys())
print(type(dic.keys()))
for di in dic.keys():
    print(di)

print(list(dic.keys())[0])
print(dic[list(dic.keys())[0]])
temp = dic[list(dic.keys())[0]]
temp.sort()
print(temp[0])

arr  = [1,2,3,4,5,6,7]
print(arr[0:3]+arr[4:])

print("df")
print("df".split())

def DFS(ans):
    ans.append(3)
    return
ans = [1]
DFS(ans)
print(ans)

aa = []
for i in aa:
    print(i)
