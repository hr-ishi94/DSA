class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None

class LinkedList:
    def __init__(self):
        self.head=None

    def printLL(self):
        if self.head is None:
            print('Linked List is empty!')
        else:
            n=self.head
            while n is not None:
                print(n.data)
                n=n.ref
    def insert_begin(self,data):
        new_node=Node(data)
        new_node.ref=self.head
        self.head=new_node

    def insert_end(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            n=self.head
            while n.ref is not None:
                n=n.ref
            n.ref=new_node
        
    def delete_end(self):
        if self.head is None:
            print('empty!')
        else:
            n=self.head
            while n.ref.ref is not None:
                n=n.ref
            n.ref=None    
           


LL1=LinkedList()
LL1.insert_begin(23)
LL1.insert_end(24)
LL1.delete_end()
LL1.printLL()