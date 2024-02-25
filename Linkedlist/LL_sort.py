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
        cpr=None
        ptr=self.head

        while ptr.ref is not None:
            cpr=ptr.ref
            while cpr is not None:
                if ptr.data>cpr.data:
                    ptr.data,cpr.data=cpr.data,ptr.data
                cpr=cpr.ref
            ptr=ptr.ref    



ll1=LinkedList()                        
ll1.add_begin(132)
ll1.add_begin(1625323345436)
ll1.add_begin(14444)
ll1.add_begin(1513414)
ll1.sort()
ll1.printLL()



        