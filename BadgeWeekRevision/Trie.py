class Trienode:
    def __init__(self):
        self.children = {}
        self.is_complete = False

    
class Trie:
    def __init__(self):
        self.root = Trienode()

    def insert(self,word):
        node = self.root 
        for char in word:
            if char not in node.children:
                node.children[char]  = Trienode()
            node = node.children[char]
        node.is_complete = True


    def search(self,word):
        node = self.root

        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]

        return node.is_complete
    
    def search_prefix(self,prefix):
        node = self.root

        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

node= Trie()
node.insert("HRISHI")
print(node.search("HRISHI"))
print(node.search_prefix("HRI"))
    
