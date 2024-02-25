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
    
    def delete_end(self):
        if self.head is None:
            print("List empty!")
            return
        elif self.head.ref is None:
            self.head =None
        else:
            n=self.head
            while n.ref.ref is not None:
                n=n.ref
            
            n.ref=None

                

LL=LinkedList()
LL.add_begin(10)
LL.add_begin(20)
LL.add_begin(30)
LL.add_begin(40)
LL.delete_end()

LL.printLL()