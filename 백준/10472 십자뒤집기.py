from collections import deque
import copy

dx = [0,-1,1,0,0]
dy = [0,0,0,-1,1]

P = int(input())

def fun(arr):
    ans = 0
    for i in range(3):
        for j in range(3):
            if arr[i][j] == '*':
                ans += 2**(3*i+j)

    return ans

for _  in range(P):
    arr = []
    check = [False]*512

    for i in range(3):
        arr.append(list(input().rstrip()))

    q = deque()
    q.append([0, [["."]*3 for i in range(3)]])
    check[0b000000000]
    while q:
        cnt, curr_arr = q.popleft()
        if curr_arr == arr:
            print(cnt)
            break

        for i in range(3):
            for j in range(3):
                new_arr = copy.deepcopy(curr_arr)
                for k in range(5):
                    new_x = i + dx[k]
                    new_y = j + dy[k]
                    if 0<=new_x<3 and 0<=new_y<3:
                        if new_arr[new_x][new_y] == '.':
                            new_arr[new_x][new_y] = '*'
                        else:
                            new_arr[new_x][new_y] = '.'

                pos = fun(new_arr)
                if check[pos] == False:
                    check[pos] = True
                    q.append([cnt+1,new_arr])


