import sys

sys.setrecursionlimit(11111)


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class binTree:
    def __init__(self, r):
        self.root = r

    def insert(self, node):
        temp = self.root
        while True:
            if node.data < temp.data:
                if temp.left == None:
                    temp.left = node
                    break
                else:
                    temp = temp.left
            else:
                if temp.right == None:
                    temp.right = node
                    break
                else:
                    temp = temp.right

    def postorder(self, node):
        if node.left != None:
            self.postorder(node.left)

        if node.right != None:
            self.postorder(node.right)
        print(node.data)


if __name__ == "__main__":
    tree = binTree(Node(int(input())))
    while True:
        try:
            tree.insert(Node(int(input())))
        except:
            break
    tree.postorder(tree.root)
