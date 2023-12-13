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


    def delete(self,data,curr):
        if not self.key:
            print('Tree is empty!')
            return
        if self.key>data:
            if self.lchild:
                self.lchild=self.lchild.delete(data,curr)
            else:
                print('Not found in Tree!')
        elif self.key<data:
            if self.rchild:
                self.rchild=self.rchild.delete(data,curr)
            else:
                print('Not found in Tree!')
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
                    self.rchild=temp.rchild
                    self.lchild=temp.lchild
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
print('Preorder')

if count(root)>1:
    root.delete(77,root.key)
else:
    print('cannot do this operation!')
root.preorder()    
print('Preorder')
