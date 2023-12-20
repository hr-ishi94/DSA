class BST:
    def __init__(self,key):
        self.key=key
        self.lchild=None
        self.rchild=None
    
    def insert(self,data):
        if not self.key:
            self.key=data
            return
        if self.key==data:
            return
        if self.key>data:
            if self.lchild:
                self.lchild.insert(data)
            else:
                self.lchild=BST(data)
        else:
            if self.rchild:
                self.rchild.insert(data)
            else:
                self.rchild=BST(data)

    def validate(self):
        if not self.key:
            print('empty root or tree!')
            return False
        if self.lchild and self.lchild.key>=self.key:
            return False
        if self.rchild and self.rchild.key<=self.key:
            return False
        
        if self.lchild and not self.lchild.validate():
            return False
        if self.rchild and not self.rchild.validate():
            return False
        return True
    
    def preorder(self):
        print(self.key,end=' ')
        if self.lchild:
            self.lchild.preorder()
        if self.rchild:
            self.rchild.preorder()
    
    def inorder(self):
        if self.lchild:
            self.lchild.inorder()
        print(self.key,end=' ')
        if self.rchild:
            self.rchild.inorder()

    def postorder(self):
        if self.lchild:
            self.lchild.postorder()
        if self.rchild:
            self.rchild.postorder()
        print(self.key,end=' ')

    def delete_node(self,data,curr):
        if self.key>data:
            if self.lchild:
                self.lchild=self.lchild.delete_node(data,curr)
            else:
                print('Node not Found!')
        elif self.key<data:
            if self.rchild:
                self.rchild=self.rchild.delete_node(data,curr)
            else:
                print('Node not Found!')
        else:
            if not self.lchild:
                temp=self.rchild
                if data==curr:
                    self.key=temp.key
                    self.lchild=temp.lchild
                    self.rchild=temp.rchild
                    return
                self=None
                return temp
            if not self.rchild:
                temp=self.lchild
                if data==curr:
                    self.key=temp.key
                    self.lchild=temp.lchild
                    self.rchild=temp.rchild
                    return

                self=None
                return temp
            node=self.rchild
            while node.lchild:
                node=node.lchild

            self.key=node.key
            self.rchild=self.rchild.delete_node(node.key,curr)
        return self
    
    def Min_node(self):
        node=self
        while node.lchild:
            node=node.lchild
        print('Min node of the Tree is ',node.key)
        return
    
    def Max_node(self):
        node=self
        while node.rchild:
            node=node.rchild
        print('Max node of the tree is :',node.key)
        return 

def count(node):
    if not node:
        return 0
    else:
        return 1+count(node.lchild)+count(node.rchild)


root=BST(None)
arr=[1,15,4,7,2,3,56,67,8,54,2,4,5,78990]
for i in arr:
    root.insert(i)

if root.validate():
    print('Tree is a BST!')
else:
    print('Not a BST!')

print('----------Preorder----------')
root.preorder()
print()
print('----------Postorder----------')
root.postorder()
print()
print('-------------------Inorder------------')
root.inorder()



print()
if count(root)>1:
    print('---------After deletion----------')
    root.delete_node(1,root.key)
else:
    print('Node cannot be deleted!')
root.preorder()




print()
print('-----------------------------------')
root.Min_node()
print('-----------------------------------')
root.Max_node()



class TrieNode:
    def __init__(self):
        self.children={}
        self.is_complete=False

class Trie:
    def __init__(self):
        self.root=TrieNode()
    
    def insert(self,word):
        node=self.root
        for char in word:
            if char not in node.children:
                node.children[char]=TrieNode()
            node=node.children[char]
        node.is_complete=True 

    def search(self,word):
        node=self.root
        for char in word:
            if char not in node.children:
                return False
            node=node.children[char]
        return node.is_complete
    
    def prefix(self,word):
        node=self.root
        for char in word:
            if char not in node.children:
                return False
            node=node.children[char]
        return True
    
print()
print('-----TRIE-----')
root=Trie()
arr=['London','NewYork','Berlin','Ottawa','New Delhi']
for i in arr:
    root.insert(i)

print('New Delhi is in Trie: ',root.search('New Delhi'))
print('London is in Trie: ',root.search('London'))
print('Paris is in Trie: ',root.search('Paris'))
print('Mumbai is in Trie: ',root.search('Mumbai'))
print('Word starting with Lon is there in Trie: ',root.prefix('Lon'))
print('Word starting with New is there in Trie: ',root.prefix('New'))
print('Word starting with Mum is there in Trie: ',root.prefix('Mum'))
print('Word starting with Otta is there in Trie: ',root.prefix('Otta'))

