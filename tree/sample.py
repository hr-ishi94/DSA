class BST:
    def __init__(self,key):
        self.key=key
        self.lchild=None
        self.rchild=None
    
    def insert_node(self,data):
        if not self.key:
            self.key=data
        if self.key==data:
            return
        if self.key>data:
            if self.lchild:
                self.lchild.insert_node(data)
            else:
                self.lchild=BST(data)
        else:
            if self.rchild:
                self.rchild.insert_node(data)
            else:
                self.rchild=BST(data)
    
    def pre_order(self):
        print(self.key,end=' ')
        if self.lchild:
            self.lchild.pre_order()
        if self.rchild:
            self.rchild.pre_order()

    def inorder(self):
        if self.lchild:
            self.lchild.inorder()
        print(self.key,end=' ')
        if self.rchild:
            self.rchild.inorder()

    def post_order(self):
        if self.lchild:
            self.lchild.post_order()
        if self.rchild:
            self.rchild.post_order()
        print(self.key,end=' ')
    
    def validate(self):

        if not self.key:
            print('Empty Tree!')
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
    
    def delete_node(self,data,curr):
        if self.key>data:
            if self.lchild:
                self.lchild=self.lchild.delete_node(data,curr)
            else:
                print('Node not found!')
        elif self.key<data:
            if self.rchild:
                self.rchild=self.rchild.delete_node(data,curr)
            else:
                print('Node not found!')
        else:
            if not self.lchild:
                temp=self.rchild
                if data==curr:
                    self.key=temp.key
                    self.lchild=temp.lchild
                    self.rchild=temp.rchild
                    temp=None
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
    
    def min_node(self):
        node=self
        while node.lchild:
            node=node.lchild
        print('Min node of the tree:',node.key)
    
    def max_node(self):
        node=self
        while node.rchild:
            node=node.rchild

        print('Max node of the tree:',node.key)

def count(self):
    if not self:
        return 0
    else:
        return 1+count(self.lchild)+count(self.rchild)

            

        


root=BST(1)
arr=[23,3,35,3,54,64,2,12,32,43,54,32,2,123,23,44,23]

for i in arr:
    root.insert_node(i)
print()
print()
print()
print('Pre-order Traversal------------>')
root.pre_order()
print()
print()
print('In-order Traversa---------->')
root.inorder()
print()
print()
print('Post-order Traversal--------->')
root.post_order()

root.delete_node(1,root.key)
print()
print()
print('After deletion')
print('Post-order Traversal--------->')
root.post_order()


valid=root.validate()
print()
print()
print()
if valid:
    print('Tree is a valid BST')
else:
    print('Tree is not a BST')

print(count(root))

root.min_node()
root.max_node()

class Trie_node:
    def __init__(self):
        self.children={}
        self.is_complete=False

class Trie:
    def __init__(self):
        self.root=Trie_node()

    def insert(self,word):
        node=self.root

        for char in word:
            if char not in node.children:
                node.children[char]=Trie_node()
            node=node.children[char]
        node.is_complete=True
    
    def search(self,word):
        node=self.root

        for char in word:
            if char not in node.children:
                return False
            node=node.children[char]
        return node.is_complete
    
    def prefix(self,pre):
        node=self.root
        for char in pre:
            if char not in node.children:
                return False
            node=node.children[char]
        return True
        
node=Trie()
node.insert('Hrishi')
node.insert('Hrishikesh')
node.insert('Hrithik')
node.insert('Sulaiman')
print(node.search('Hrishi'))
print(node.search('Hrishikesh'))
print(node.search('suka'))
print(node.search('Sulaiman'))
print(node.prefix('Hrishi'))
print(node.prefix('Hri'))
print(node.prefix('Sul'))


print('Heap')
import heapq

arr1=[33,12,2,23,35,654,67]
heapq.heapify(arr1)
heapq.heappush(arr1,1)
heapq.heappop(arr1)
heapq.heappushpop(arr1,12)
heapq.heapreplace(arr1,1)
print(heapq.nlargest(2,arr1))
print(heapq.nsmallest(1,arr1))
print(arr1)


list3=[(11,'hrishi'),(7,'prasad'),(3,'hrishikesh')]
heapq.heapify(list3)
for i in list3:
    print(i)