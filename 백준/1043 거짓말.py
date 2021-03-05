import sys

input = sys.stdin.readline


class Node:
    def __init__(self, data):
        self.item = data
        self.parent = data
        self.rank = 1


class DisjointSet:
    def __init__(self, n):
        # 1. 초기화
        self.node_list = [{} for _ in range(n + 1)]
        for x in range(1, n + 1):
            self.node_list[x] = Node(x)

    def find(self, u):
        if u == self.node_list[u].parent:
            return u

        # 경로압축.
        # 다음번 연산에서 반복해서 올라갈 필요없이 바로 루트노드로 갈 수 있다.
        self.node_list[u].parent = self.find(self.node_list[u].parent)
        return self.node_list[u].parent

    def union(self, u, v):
        u = self.find(u)
        v = self.find(v)

        if u == v:
            return

        if self.node_list[u].rank > self.node_list[v].rank:
            u, v = v, u
        self.node_list[u].parent = v

        if self.node_list[u].rank == self.node_list[v].rank:
            self.node_list[v].rank += 1


if __name__ == "__main__":
    N, M = map(int, input().split())
    temp = list(map(int, input().split()))
    truth_num = temp[0]

    if truth_num != 0:
        truth_numbers = temp[1:]
    else:
        print(M)
        exit(0)

    disjointTree = DisjointSet(N)

    parties = []
    for i in range(M):
        parties.append(list(map(int, input().split())))
        for j in range(1, parties[-1][0]):
            disjointTree.union(parties[-1][1], parties[-1][j + 1])

    truth_root = set()
    for i in temp[1:]:
        truth_root.add(disjointTree.find(disjointTree.node_list[i].item))

    can_lie = set()
    for i in range(1, N + 1):
        if disjointTree.find(disjointTree.node_list[i].item) not in truth_root:
            can_lie.add(i)

    ans = 0
    for member in parties:
        if member[0] == 0:
            ans += 1
        else:
            temp_set = set(member[1:])
            if len(temp_set - can_lie) == 0:
                ans += 1

    print(ans)
