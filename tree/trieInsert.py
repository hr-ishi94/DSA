class Node:
    def __init__(self):
        self.children={}
        self.end=False

class Trie:
    def __init__(self):
        self.root=Node()

    def insert(self,word):
        node=self.root
        for char in word:
            if char not in node.children:
                node.children[char]=Node()
            node=node.children[char]
        node.end=True

    def search(self,word):
        node=self.root
        for char in word:
            if char not in node.children:
                return False
            node=node.children[char]
        return node.end
    
    def prefix(self,word):
        node=self.root
        for char in word:
            if char not in node.children:
                return False
            node=node.children[char]
        return True

root=Trie()

root.insert('HRISHI')
res=root.search('HRISHI')
print(root.prefix('HR'))
print(res)