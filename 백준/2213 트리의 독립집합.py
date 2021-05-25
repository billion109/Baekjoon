import sys

input = sys.stdin.readline


def postorder(node):
    for i in edge_list[node]:
        if check[i]:
            check[i] = False
            node_list[node].child.append(i)
            postorder(i)

    if node != root_node and len(edge_list[node]) == 1:
        node_list[node].dp = node_list[node].val
        node_list[node].dp_list.append(node_list[node].num)
        return

    child_val = 0
    not_child_val = 0
    temp1 = []
    temp2 = []

    for i in node_list[node].child:
        child_val += node_list[i].dp
        temp1 += node_list[i].dp_list
        for j in node_list[i].child:
            not_child_val += node_list[j].dp
            temp2 += node_list[j].dp_list
    not_child_val += node_list[node].val
    temp2.append(node_list[node].num)

    if not_child_val >= child_val:
        node_list[node].dp = not_child_val
        node_list[node].dp_list += temp2
    else:
        node_list[node].dp = child_val
        node_list[node].dp_list += temp1


class Node:
    def __init__(self, num, val):
        self.num = num
        self.val = val
        self.dp = 0
        self.dp_list = []
        self.child = []


n = int(input())
arr = list(map(int, input().split()))
node_list = [0]
check = [True for _ in range(n + 1)]

for i in range(n):
    node_list.append(Node(i + 1, arr[i]))

edge_list = [[] for _ in range(n + 1)]
for i in range(n - 1):
    u, v = map(int, input().split())
    edge_list[u].append(v)
    edge_list[v].append(u)

root_node = 0
for i in range(n + 1):
    if len(edge_list[i]) == 1:
        root_node = i
        break
check[root_node] = False
postorder(root_node)
print(node_list[root_node].dp)
node_list[root_node].dp_list.sort()
print(*node_list[root_node].dp_list)
