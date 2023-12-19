class BST:
    def __init__(self,key):
        self.key=key
        self.lchild=None
        self.rchild=None

    def insert(self,data):
        if self.key is None:
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

    def search(self,data):
        if self.key==data:
            print('found!')
            return
        if self.key>data:
            if self.lchild:
                self.lchild.search(data)
            else:
                print('not found!')
        else:
            if self.rchild:
                self.rchild.search(data)
            else:
                print('not found!')
    
    def delete(self,data,curr):
        if not self.key:
            print('Empty tree!')
            return
        if self.key>data:
            if self.lchild:
                self.lchild=self.lchild.delete(data,curr)
            else:
                print('not found in tree!')
        elif self.key<data:
            if self.rchild:
                self.rchild=self.rchild.delete(data,curr)
            else:
                print('Not found in tree!')
        else:
            if not self.lchild:
                temp=self.rchild
                if curr==data:
                    self.key=temp.key
                    self.rchild=temp.rchild
                    self.lchild=temp.lchild
                    temp= None
                    return
                self=None
                return temp
            if not self.rchild:
                temp=self.lchild
                if curr==data:
                    self.key=temp.key
                    self.lchild=temp.lchild
                    self.rchild=temp.rchild
                    temp=None
                    return 
                self=None
                return temp
            node=self.rchild
            while node.lchild:
                node=node.lchild
            self.key=node.key
            self.rchild=self.rchild.delete(node.key,curr)
        return self
    
    def min_node(self):
        node=self
        while node.lchild:
            node=node.lchild
        print(node.key)
        return    
    def max_node(self):
        node=self
        while node.rchild:
            node=node.rchild
        print(node.key)
        return
            



def count(root):
    if not root:
        return 0
    else:
        return 1+count(root.lchild)+count(root.rchild)


root=BST(None)
arr=[2,4,5,6,77,8,3,45,7]

for i in arr:
    root.insert(i)
    
root.preorder()
print('preorder')
root.inorder()
print('inorder')
root.postorder()
print('postorder')

root.search(7)

if count(root)>1:
    root.delete(2,root.key)
else:
    print('cannot be deleted!')

root.postorder()
print('postorder')

print('Min Node of the tree!')
root.min_node()
print('max Node of the tree!')
root.max_node()


#HEAP
print('--------Heap DS---------')
import heapq
list1=[]
heapq.heappush(list1,12)
heapq.heappush(list1,1)
heapq.heappush(list1,16)
heapq.heappush(list1,21)
heapq.heappush(list1,17)
heapq.heappush(list1,5)
heapq.heappush(list1,2)
print(list1)

heapq.heappop(list1)
heapq.heappushpop(list1,3)
heapq.heapreplace(list1,6)
print(list1)
list2=[2,6,6,7,34,23,12,56,565]
heapq.heapify(list2)
print(list2)
print(heapq.nsmallest(3,list2))
print(heapq.nlargest(3,list2))

list3=[(1,'hrishi'),(1,'prasad'),(3,'hrishikesh')]

heapq.heapify(list3)
for i in range(len(list3)):
    print(heapq.heappop(list3))