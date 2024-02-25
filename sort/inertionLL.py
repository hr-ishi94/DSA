class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None

class LinkedList:
    def __init__(self):
        self.head= None

    def add_begin(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            new_node.ref=self.head
            self.head=new_node
    def printLL(self):
        n=self.head
        while n is not None:
            print(n.data,'-->',end='')
            n=n.ref
    def sort(self):
        prev=None
        n=self.head 

        
ll=LinkedList()
ll.add_begin(80)
ll.add_begin(40)
ll.add_begin(30)
ll.add_begin(50)
ll.printLL()                        