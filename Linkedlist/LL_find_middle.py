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

    def middle(self):
        if self.head is None:
            print('empty list!')
            return
        s=self.head
        f=self.head.ref
        while f is not None and f.ref is not None:
            f=f.ref.ref
            s=s.ref
        print('middle value of the Linked List is :',s.data)
                

ll1=LinkedList()                        
ll1.add_begin(13)
ll1.add_begin(14)
ll1.add_begin(15)
ll1.add_begin(16)
ll1.add_begin(17)
ll1.printLL()
ll1.middle()



        