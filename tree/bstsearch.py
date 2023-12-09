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

    def search(self,data):
        if self.key==data:
            print('found at root!')
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






root=BST(10)
arr=[2,3,5,6,7,8,43]

for i in arr:
    root.insert(i)

root.search(23)

