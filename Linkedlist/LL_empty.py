class Node:
    def __init__(self,data):
        self.data=data
        self.ref= None

class LinkedList:
    def __init__(self):
        self.head=None
    
    def printLL(self):
        if self.head is None:
            print('Linked list is empty!')
        else:
            n=self.head
            while n is not None:
                print(n.data,end=' ')
                n=n.ref

    def add_empty(self,data):
        if self.head is None:
            new_node=Node(data)
            self.head=new_node
        else:
            print('list is not empty!')    





ll1=LinkedList()                        
ll1.add_empty(100)
ll1.add_empty(200)
ll1.add_empty(300)
ll1.add_empty(400)
ll1.printLL()





