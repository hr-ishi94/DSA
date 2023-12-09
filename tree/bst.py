class BST:
    def __init__(self,key):
        self.key=key
        self.lchild=None
        self.rchild=None

root=BST(12)
root.lchild=BST(6)
root.rchild=BST(18)
root.rchild.lchild=BST(15)
root.rchild.rchild=BST(20)
print(root.key)
print(root.lchild,root.lchild.key)
print(root.rchild,root.rchild.key)
print(root.rchild.lchild,root.rchild.lchild.key)
print(root.rchild.rchild,root.rchild.rchild.key)
