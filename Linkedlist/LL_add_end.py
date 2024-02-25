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

   
    
    def add_end(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            n=self.head
            while n.ref is not None:
                n=n.ref
            n.ref =new_node    


ll1=LinkedList()                        

arr=[10,20,30,40,50]
for i in arr:
    ll1.add_end(i)


ll1.printLL()





