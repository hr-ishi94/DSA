class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None

class LinkedList:
    def __init__(self):
        self.head= None

    def printLL(self):
        if not self.head:
            print("Empty linked list!")
        else:
            n=self.head
            while n:
                print(n.data,"--> ",end="")
                n=n.ref

    def add_begin(self,data):
        node= Node(data)
        node.ref = self.head
        self.head = node

    def add_end(self,data):
        node= Node(data)
        if not self.head:
            self.head= node
        else:
            n=self.head
            while n.ref:
                n=n.ref
            n.ref= node

    def add_after(self,data,x):
        if not self.head:
            print("Linked list is Empty !")
            return

        new_node= Node(data)

        if self.head.data==x:
            new_node.ref=self.head.ref
            self.head.ref=new_node
        else:
            n=self.head
            while n:
                if n.data==x:
                    break
                n=n.ref
            if not n:
                print(x,' is not not found!')
                return
            new_node.ref=n.ref
            n.ref=new_node
            return 
        
    def add_before(self,data,x):
        if not self.head:
            print("Linked list is empty!")
            return

        new_node= Node(data)

        if self.head.data==x:
            new_node.ref=self.head
            self.head=new_node
        else:
            n=self.head
            while n.ref:
                if n.ref.data==x:
                    break
                n=n.ref
            if not n.ref:
                print(x," is not found!")
                return
            new_node.ref=n.ref
            n.ref= new_node
            return
    
    def delete_begin(self):
        if not self.head:
            print("Empty linked list!")
            return 
        self.head= self.head.ref
        return
    
    def delete_end(self):
        if not self.head:
            print("Empty linked list!")
            return
        if not self.head.ref:
            self.head=self.head.ref
        else:
            n= self.head
            while n.ref.ref:
                n=n.ref
            n.ref= None
    def delete_val(self,x):
        if not self.head:
            print("Empty linked list!")
            return
        if self.head.data == x:
            self.head= self.head.ref
        else:
            n=self.head
            while n:
                if n.ref.data == x:
                    break
                n=n.ref
            if not n:
                print(x," is not found!")
                return
            n.ref = n.ref.ref

            


LL= LinkedList()
LL.add_begin(12)
LL.add_begin(11)
LL.add_end(15)
LL.add_end(17)
LL.add_end(13)
LL.add_after(19,13)
LL.add_before(20,11)
LL.delete_begin()
LL.delete_end()
LL.delete_val(11)
LL.delete_val(15)
LL.delete_val(17)
LL.delete_val(13)
LL.printLL()