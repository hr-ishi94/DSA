class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None

class LinkedList:
    def __init__(self):
        self.head=None

    def add_begin(self,data):
        new_node=Node(data)
        new_node.ref=self.head
        self.head=new_node
    
    def length(self):
        length=0
        if self.head is None:
            print('Empty list!!')
        else:
            n=self.head
            while n is not None:
                length+=1
                n=n.ref
            print('Length of the linked list is',length)

LL=LinkedList()
LL.add_begin(12)
LL.add_begin(12)
LL.add_begin(12)
LL.length()