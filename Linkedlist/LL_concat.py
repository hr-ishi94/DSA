class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None

class LinkedList:
    def __init__(self):
        self.head1=None
        self.head2=None
    
    def add_begin(self,data2,data1):
        node1=Node(data1)
        node2=Node(data2)
        node1.ref=self.head1
        self.head1=node1
        node2.ref=self.head2
        self.head2=node2

    def printLL(self):
        n1=self.head1
        n2=self.head2
        while n1 is not None:
            print(n1.data,'-->',end=' ')
            n1=n1.ref
        print()    
        while n2 is not None:
            print(n2.data,'-->',end=' ')
            n2=n2.ref

    def concat(self):
        n1=self.head1
        while n1.ref is not None:
            n1=n1.ref
        n1.ref=self.head2
        
                 


LL=LinkedList()
LL.add_begin(11,16)
LL.add_begin(12,17)
LL.add_begin(13,18)
LL.add_begin(14,19)
LL.add_begin(15,20)
LL.concat()

LL.printLL()



