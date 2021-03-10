import sys

input = sys.stdin.readline


class Node:
    def __init__(self, item):
        self.item = item


class Tree:
    def __init__(self, num):
        self.node_list = [{} for _ in range(num + 1)]
        self.num = num

    def insert(self, u, v, w):
        self.node_list[u][v] = w


if __name__ == "__main__":
    V = int(input().rstrip())
    tree = Tree(V)
    for _ in range(V - 1):
        u, v, w = list(map(int, input().split()))
        tree.insert(u, v, w)
        tree.insert(v, u, w)

    # 1부터 가장 먼 노드를 찾기
    check = [True] * (V + 1)
    val = [0] * (V + 1)
    q = []
    q.append([tree.node_list[1], 0])
    check[1] = False
    while len(q) > 0:
        connected_node, cnt = q.pop()
        for node, weight in connected_node.items():
            if check[node]:
                check[node] = False
                q.append([tree.node_list[node], cnt + weight])
                val[node] = cnt + weight

    end_node = val.index(max(val))

    # 가장 먼 노드로부터 DFS를 사용하여 최장거리 찾기
    check = [True] * (V + 1)
    val = [0] * (V + 1)
    q = []
    q.append([tree.node_list[end_node], 0])
    check[end_node] = False
    while len(q) > 0:
        connected_node, cnt = q.pop()
        for node, weight in connected_node.items():
            if check[node]:
                check[node] = False
                q.append([tree.node_list[node], cnt + weight])
                val[node] = cnt + weight

    print(max(val))
