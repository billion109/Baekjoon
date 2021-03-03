import sys
from collections import deque

input = sys.stdin.readline


class Node:
    def __init__(self, item):
        self.data = item
        self.parent = None
        self.child = []

if __name__ == "__main__":
    N = int(input())
    node_list = [None for _ in range(N + 1)]
    for i in range(1, N + 1):
        node_list[i] = Node(i)

    for i in range(N - 1):
        a, b = map(int, input().split())
        node_list[a].child.append(b)
        node_list[b].child.append(a)

    check = [False for _ in range(N+1)]
    check[1] = True
    q = deque([])
    q.append(node_list[1])
    while len(q)>0:

        temp_node = q.popleft()
        for node in temp_node.child:
            if check[node] == True:
                continue
            node_list[node].parent = temp_node.data
            check[node] = True
            q.append(node_list[node])

    for i in range(2, N+1):
        print(node_list[i].parent)