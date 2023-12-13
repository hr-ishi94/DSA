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


    def delete(self,data):
        if not self.key:
            print('Tree is empty!')
            return
        if self.key>data:
            if self.lchild:
                self.lchild=self.lchild.delete(data)
            else:
                print('Not found in Tree!')
        elif self.key<data:
            if self.rchild:
                self.rchild=self.rchild.delete(data)
            else:
                print('Not found in Tree!')
        else:
            if not self.lchild:
                temp=self.rchild
                self=None
                return temp
            if not self.rchild:
                temp=self.lchild
                self=None
                return temp
            node=self.rchild
            while node.lchild:
                node=node.lchild
            self.key=node.key
            self.rchild=self.rchild.delete(node.key)

        return self
    
    def min(self):
        curr=self
        while curr.lchild:
            curr=curr.lchild
        print('Min value of the tree is:',curr.key)
    def max(self):
        curr=self
        while curr.rchild:
            curr=curr.rchild
        print('Max value of the tree is :',curr.key)
root=BST(None)
arr=[2,4,5,6,77,8,3,45,7]
for i in arr:
    root.insert(i)
root.preorder()    
print('Preorder')
# root.inorder()    
# print('Inorder')
# root.postorder()    
# print('Postorder')

root.delete(10)

root.preorder()    
print('Preorder')

root.min()
root.max()
