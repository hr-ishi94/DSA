class BST:

    def __init__(self,key):
        self.key = key
        self.lchild = None
        self.rchild = None
    
    def insert(self,data):
        if not self.key :
            self.key = data
            return 
        
        if self.key == data:
            return 
        
        if data<self.key:
            if self.lchild:
                self.lchild.insert(data)
            else:
                self.lchild = BST(data)
        else:
            if self.rchild :
                self.rchild.insert(data)
            else:
                self.rchild = BST(data)

    def pre_order(self):
        print(self.key,"-->",end =" ")
        
        if self.lchild:
            self.lchild.pre_order()    
        if self.rchild:
            self.rchild.pre_order()

    def in_order(self):
        if self.lchild:
            self.lchild.in_order()
        print(self.key,'-->',end= "")
        if self.rchild:
            self.rchild.in_order()

    def post_order(self):
        if self.lchild:
            self.lchild.post_order()
        if self.rchild:
            self.rchild.post_order()
        print(self.key, "-->", end=" ")

    # def delete(self,data):

    #     if not self.key:
    #         print("Empty tree!")
    #         return 
        
    #     if data < self.key:
    #         if self.lchild:
    #             self.lchild = self.lchild.delete(data)
    #         else:
    #             print("Node not found !")
    #     elif data >self.key:
    #         if self.rchild:
    #             self.rchild = self.rchild.delete(data)
    #         else:
    #             print("Node not found!")
    #     else:
    #         if not self.lchild:
    #             temp = self.rchild
    #             self = None
    #             return temp
    #         if not self.rchild:
    #             temp = self.lchild
    #             self = None
    #             return temp
    #         node = self.rchild
    #         while node.lchild:
    #             node = node.lchild
    #         self.key = node.key
    #         self.rchild = self.rchild.delete(node.key)

    #     return self

    def delete(self,data,curr):
        if not self.key:
            print("tree empty!")
            return 
        
        if self.key > data:
            if self.lchild:

                self.lchild = self.lchild.delete(data,curr)
            else:
                print("Node not found!")
        elif self.key < data:
            if self.rchild :
                self.rchild = self.rchild.delete(data, curr)
            else:
                print("Node not found!")
        else:
            if not self.lchild:
                temp = self.rchild
                if data == curr:
                    self.key = temp.key
                    self.lchild = temp.lchild
                    self.rchild = temp.rchild
                    return 
                self = None
                return temp
            if not self.rchild:
                temp = self.lchild
                if data == curr:
                    self.key = temp.key
                    self.lchild = temp.lchild
                    self.rchild = temp.rchild
                    return 

                self = None
                return temp
            
            node = self.rchild
            
            while node.lchild:
                node = node.lchild
            
            self.key = node.key
            self.rchild= self.rchild.delete(node.key,curr)

        return self

    def min_node(self):
        node = self
        while node.lchild:
            node = node.lchild

        print("min node is ", node.key)
        return 
    
    def max_node (self):
        node = self
        while node.rchild:
            node = node.rchild
        print("Max node is ", node.key)


    def validator(self):
        if not self.key:
            return False
        
        if self.lchild and self.lchild.key >= self.key:
            return False
        if self.rchild and self.rchild.key <= self.key:
            return False
        
        if self.lchild and self.lchild.validator():
            return False
        
        if self.rchild and self.rchild.validator():
            return False
        
        return True
    
def count_nodes(self):
    if not self:
        return 0
    else:
        return 1 + count_nodes(self.lchild)+ count_nodes(self.rchild)


root = BST(None)
arr = [3,4,2,12,56,22,43,1,7]

for x in arr:
    root.insert(x) 

root.pre_order()
print("")
root.delete(3,root.key)
root.delete(4,root.key)
root.pre_order()
print("")
root.min_node()
root.max_node()

if root.validator():
    print("Yes it is a binary tree!")
else:
    print("not a binary tree")


print(count_nodes(root))

# print("")
# root.in_order()
# print("")
# root.post_order()


