class Node():
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList():
    def __init__(self, head, tail):
        self.head = head
        self.tail = tail

    def push(self, node):
        self.tail.next = node
        self.tail = node

    def pop(self):
        temp = self.head
        self.head = self.head.next
        return temp


node = Node(1)
list = LinkedList(node, node)
list.push(Node(3))
list.push(Node(8))
print(list.pop().val)
print(list.pop().val)

