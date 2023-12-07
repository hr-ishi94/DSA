class Node:
    def __init__ (self,data):
        self.data=data
        self.ref=None

class LinkedList:
    def __init__(self):
        self.head=None

    def push(self,data):
        new_node=Node(data)
        new_node.ref=self.head
        self.head=new_node
    
    def bubble(self):
        if not self.head or not self.head.ref:
            return self.head
        bsort=False
        while not bsort:
            bsort =True
            curr=self.head
            while curr.ref:
                if curr.data>curr.ref.data:
                    curr.data,curr.ref.data=curr.ref.data,curr.data
                    bsort=False
                curr=curr.ref
        return self.head

    def printLL(self):
        n=self.head
        while n:
            print(n.data,'-->',end='')
            n=n.ref


LL=LinkedList()
LL.push(11)                    
LL.push(12)                    
LL.push(13)                    
LL.push(14)                    
LL.push(15)                    
LL.push(16)
LL.bubble()
LL.printLL()                    




