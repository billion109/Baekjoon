from collections import deque
import sys
sys.setrecursionlimit(10**5+100)


class Node:
    def __init__(self, item):
        self.item = item
        self.child = []
        self.ans = 1


class Tree:
    def __init__(self, r, n, m):
        self.root = r
        self.childs = [Node(i) for i in range(n + 1)]
        self.childs[m] = r

    def post(self, node):
        # print("입력은",node)
        if self.childs[node].child:
            for i in self.childs[node].child:
                self.childs[node].ans += self.post(i)
        else:
            self.childs[node].ans = 1

        # print("반환한다.",node,self.childs[node].ans)
        return self.childs[node].ans


N, R, Q = map(int, input().split())
adjacent = [{} for _ in range(N + 1)]
for i in range(N - 1):
    u, v = map(int, input().split())
    adjacent[u][v] = 1
    adjacent[v][u] = 1

arr = []
check = [True for _ in range(N + 1)]
for i in range(Q):
    arr.append(int(input()))

tree = Tree(Node(R), N, R)
q = deque()
check[R] = False
q.append([R, adjacent[R].keys()])
while q:
    curr, keys = q.popleft()
    for key in keys:
        if check[key]:
            check[key] = False
            q.append([key, adjacent[key].keys()])
            tree.childs[curr].child.append(key)

tree.post(R)
for i in arr:
    print(tree.childs[i].ans)