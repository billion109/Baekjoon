import sys

input = sys.stdin.readline


class Node:
    def __init__(self, item, left, right):
        self.data = item
        self.left = left
        self.right = right

    def prefix(self):
        traversal = []
        traversal += self.data
        if self.left != '.':
            traversal += dic[self.left].prefix()
        if self.right != '.':
            traversal += dic[self.right].prefix()

        return traversal

    def infix(self):
        traversal = []
        if self.left != '.':
            traversal += dic[self.left].infix()
        traversal += self.data
        if self.right != '.':
            traversal += dic[self.right].infix()

        return traversal

    def postfix(self):
        traversal = []
        if self.left != '.':
            traversal += dic[self.left].postfix()
        if self.right != '.':
            traversal += dic[self.right].postfix()
        traversal += self.data

        return traversal


class BinTree:
    def __init__(self, r):
        self.root = r


N = int(input())
dic = dict()
for i in range(N):
    curr, child1, child2 = input().split()
    node = Node(curr, child1, child2)
    if i == 0:
        binTree = BinTree(node)
    dic[curr] = node

print(''.join(binTree.root.prefix()))
print(''.join(binTree.root.infix()))
print(''.join(binTree.root.postfix()))
