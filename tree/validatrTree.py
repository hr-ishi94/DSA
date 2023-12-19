class BST:
    def __init__(self,key):
        self.key=key
        self.lchild=None
        self.rchild=None

    def add_node(self,data):
        if not self.key :
            self.key=data

        if self.key==data:
            return
        
        if self.key>data:
            if self.lchild:
                self.lchild.add_node(data)
            else:
                self.lchild=BST(data)
        else:
            if self.rchild:
                self.rchild.add_node(data)
            else:
                self.rchild=BST(data)

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

            

        
    
    

root=BST(None)
arr=[2,4,5,23,65,123,23]
for i in arr:
    root.add_node(i)

print(root.key)
res=root.validate()

if res:
    print('Tree is a BST!')
else:
    print('Tree is not a BST!')    







