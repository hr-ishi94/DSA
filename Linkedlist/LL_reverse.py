class Node:
    def __init__(self,data):
        self.data=data
        self.ref =None

class LinkedList:
    def __init__(self):
        self.head=None

    def printLL(self):
        if self.head is None:
            print('Linked list is empty!!')
        else:
            n=self.head
            while n is not None:
                print(n.data ,'-->',end=' ')
                n=n.ref

    def add_begin(self,data):
        new_node=Node(data)
        new_node.ref=self.head
        self.head= new_node

    def reverse(self):
        if self.head is None:
            print('List empty!')
            return
        if self.head.ref is None:
            print('already in reversed format!')
            return
        
        prev=None
        
        current=self.head

        while current is not None:
            next=current.ref
            current.ref=prev
            prev=current
            current=next
        self.head=prev   


ll1=LinkedList()                        
ll1.add_begin(13)
ll1.add_begin(14)
ll1.add_begin(15)
ll1.add_begin(16)
ll1.reverse()
ll1.printLL()



        