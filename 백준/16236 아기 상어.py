import sys
from collections import deque
from queue import PriorityQueue
input = sys.stdin.readline
N = int(input())
arr = []
curr_size = 2
ate_num = 0
ate_queue = PriorityQueue()
can_pass = [0,1,2,9]
can_eat = [1]
time = 0


for i in range(N):
    t = list(map(int,input().split()))
    if 9 in t:
        curr_pos = [i,t.index(9)]
    arr.append(t)


while True:
    dest = -1
    visited = []
    bfs_stack = deque([curr_pos])
    while len(bfs_stack) > 0:
        curr_pos = bfs_stack.popleft()
        x, y = curr_pos[0], curr_pos[1]
        if curr_pos not in visited:
            visited.append(curr_pos)
        if arr[x][y] not in can_pass:
            continue

        if x > 0 and ([x - 1, y] not in visited) and ([x - 1, y] not in bfs_stack):
            bfs_stack.append([x - 1, y])
        if x < N - 1 and ([x + 1, y] not in visited) and ([x + 1, y] not in bfs_stack):
            bfs_stack.append([x + 1, y])
        if y > 0 and ([x, y - 1] not in visited) and ([x, y - 1] not in bfs_stack):
            bfs_stack.append([x, y - 1])
        if y < N - 1 and ([x, y + 1] not in visited) and ([x, y + 1] not in bfs_stack):
            bfs_stack.append([x, y + 1])

        if arr[x][y] in can_eat:
            ate_num += 1
        if ate_num == curr_size:
            ate_num = 0
            curr_size += 1
            can_pass.append(curr_size)
            can_eat.append(curr_size - 1)


        print(curr_pos, curr_size, arr[x][y], ate_num)
        # print(bfs_stack,curr_pos, visited)



    if dest == -1:
        break

    time+=dest

print(time)




#제자리에서 bfs 돌린후에, 거리에 따라 이동시킴.
#이동하여 먹은후에 다시 bfs돌림.