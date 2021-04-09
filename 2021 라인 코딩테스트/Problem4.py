class Node:
    def __init__(self, node_id, char, parent_id):
        self.node_id = node_id
        self.char = char
        self.parent_id = parent_id
        self.child = []


class Tree:
    def __init__(self, data):
        self.nodes = [{} for _ in range(len(data) + 1)]
        self.nodes[0] = Node(0, "ROOT", None)
        self.leaf_nodes = []
        self.length = len(data)

        for d in data:
            node_id, char, parent_id = d.split()
            node_id, parent_id = int(node_id), int(parent_id)
            self.nodes[node_id] = Node(node_id, char, parent_id)
            self.nodes[parent_id].child.append(node_id)

        for i in reversed(range(len(data)+1)):
            if not self.nodes[i].child:
                self.leaf_nodes.append(i)

    def search(self, word):
        arr = []
        for i in self.leaf_nodes:
            if word in self.nodes[i].char:
                arr.append(i)

        temp = []
        if word in arr:
            temp.append(word)
            word.remove(word)
        arr = sorted(arr, key=lambda x: (-self.nodes[x].char.count(word), self.nodes[x].char.index(word)))
        temp += arr
        arr = temp


        ans = []
        for node in arr:
            ans.append(self.show(node))

        if not ans:
            ans.append("Your search for ("+word+") didn't return any results")

        return ans

    def show(self,node):
        temp = []
        while self.nodes[node] != self.nodes[0]:
            temp.append(self.nodes[node].char)
            node = self.nodes[node].parent_id
        temp = "/".join(reversed(temp))
        return temp



def solution(data, word):
    tree = Tree(data)
    answer = tree.search(word)
    return answer


if __name__ == "__main__":
    data = [["1 BROWN 0", "2 CONY 0", "3 DOLL 1", "4 DOLL 2", "5 LARGE-BROWN 3", "6 SMALL-BROWN 3", "7 BLACK-CONY 4",
             "8 BROWN-CONY 4"],
            ["1 BROWN 0", "2 CONY 0", "3 DOLL 1", "4 DOLL 2", "5 LARGE-BROWN 3", "6 SMALL-BROWN 3", "7 BLACK-CONY 4",
             "8 BROWN-CONY 4"],
            ["1 ROOTA 0", "2 AA 1", "3 ZZZ 1", "4 AABAA 1", "5 AAAAA 1", "6 AAAA 1", "7 BAAAAAAA 1", "8 BBAA 1",
             "9 CAA 1", "10 ROOTB 0", "11 AA 10"]]
    word = ["BROWN", "SALLY", "AA"]
    for i in range(len(data)):
        solution(data[i], word[i])
        print('------------')
