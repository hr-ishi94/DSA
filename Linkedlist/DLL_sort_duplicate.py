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

    def sort(self):
        if self.head is None:
            print('empty List!')
            return 
        else:
            ptr=self.head
            while ptr.ref is not None:
                cpr=ptr.ref
                while cpr is not None:
                    if ptr.data>cpr.data:
                        ptr.data,cpr.data= cpr.data,ptr.data
                    cpr=cpr.ref
                ptr=ptr.ref

    def duplicates(self):
        if self.head is None:
            print('empty list!')
            return
        else:
            n=self.head
            while n.ref is not None:
                if n.data==n.ref.data:
                    n.ref=n.ref.ref
                    continue
                n=n.ref





ll1=LinkedList()                        
ll1.add_begin(10)
ll1.add_begin(16)
ll1.add_begin(14)
ll1.add_begin(14)
ll1.add_begin(14)
ll1.add_begin(17)
ll1.add_begin(17)
ll1.add_begin(17)
ll1.sort()
ll1.duplicates()
ll1.printLL()
