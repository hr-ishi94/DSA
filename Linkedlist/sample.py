class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None

class LinkedList:
    def __init__(self):
        self.head=None

    def add_begin(self,data):
        new_node=Node(data)
        new_node.ref=self.head
        self.head=new_node

    def find(self,x):
        n=self.head
        m=None
        count=0
        while n.ref is not None:
            m=n.ref
            while m.ref is None:
                if m.data==x:
                    count+=1
                m=m.ref
                    
