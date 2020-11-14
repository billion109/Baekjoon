import sys
input = sys.stdin.readline

def distance(a,b):
    return abs(a[0]-b[0])+abs(a[1]-b[1])


N = int(input())
car1, car2 = [1,1],[N,N]

W_num = int(input())
W_list = []
for i in range(W_num):
    W_list.append(list(map(int,input().split())))


print(W_list)