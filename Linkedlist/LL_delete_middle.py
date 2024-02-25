class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None

class LinkedList:
    def __init__(self):
        self.head=None

    def printLL(self):
        if self.head is None:
            print('Linked list not found!')
        else:
            n=self.head
            while n is not None:
                print(n.data,end=' ')
                n=n.ref

    def add_begin(self,data):
        new_node=Node(data)
        new_node.ref=self.head
        self.head=new_node
    
    def delete_middle(self,data):
        if self.head is None:
            print('Linked list is empty!')
            return
        if self.head.data==data:
            self.head=self.head.ref
            return 
        
        n=self.head
        while n.ref is not None:
            if n.ref.data==data:
                break
            n=n.ref
        if n.ref is None:
            print('Node not found!')
        else:
            n.ref=n.ref.ref

                

LL=LinkedList()
LL.add_begin(10)
LL.add_begin(20)
LL.add_begin(30)
LL.add_begin(40)
LL.delete_middle(40)

LL.printLL()