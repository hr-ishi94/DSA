class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None

class LinkedList:
    def __init__(self):
        self.head= None

    def PrintLL(self):
        if self.head is None:
            print('List empty.!')
        else:
            n=self.head
            while n is not None:
                print(n.data,'-->',end=" ")
                n=n.ref
    def reverse(self): 
        prev = None
        current = self.head 
        while(current is not None): 
            next = current.ref
            current.ref = prev 
            prev = current 
            current = next
        self.head = prev 

    def add_begin(self,data):
        new_node= Node(data)
        new_node.ref=self.head
        self.head=new_node       

LL=l=LinkedList()
LL.add_begin(10)
LL.add_begin(20)
LL.add_begin(30)
LL.add_begin(40)
LL.reverse()
LL.PrintLL()