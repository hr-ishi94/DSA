class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None

class LinkedList:
    def __init__(self):
        self.head2=None
        self.head1=None

    def add_begin(self,data1,data2):
        new_node1=Node(data1)
        new_node2=Node(data2)
        new_node1.ref=self.head1
        self.head1=new_node1
        new_node2.ref=self.head2
        self.head2=new_node2
    def merge(self):
        n1=self.head1
        n2=self.head2
        while n1.ref is not None:
            n1=n1.ref
        n1.ref=n2    

    def printLL(self):
        n1=self.head1
        n2=self.head2
        while n1 is not None:
            print(n1.data,'-->',end="")
            n1=n1.ref    
        print()    
       



LL=LinkedList()
LL.add_begin(10,12)
LL.add_begin(14,16)
LL.add_begin(15,18)
LL.add_begin(17,11)
LL.add_begin(19,10)
LL.add_begin(23,13)
LL.merge()
LL.printLL()




        