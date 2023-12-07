class Node:
    def __init__(self,data):
        self.data=data
        self.ref= None

class LinkedList:
    def __init__(self):
        self.Top=None

    def push(self,data):
        new_node=Node(data)
        new_node.ref=self.Top
        self.Top=new_node

    def pop(self):
        if self.Top is None:
            return None
        popdata=self.Top.data
        self.Top=self.Top.ref
        return popdata
    
    def peek(self):
        if self.Top:
            print(self.Top.data)
            return
        else:
            print('empty!!!!')
            return
    
    def is_empty(self):
        return self.Top.data is None
    
    def print(self):
        if self.Top is None:
            print('EMPTY LIST!!')
            return
        else:
            n=self.Top
            while n:
                print(n.data,'-->',end='')
                n=n.ref

    


LL=LinkedList()
LL.push(15)
LL.push(16)
LL.push(17)
LL.push(18)
LL.push(19)
LL.push(20)
LL.pop()
LL.is_empty()
LL.peek()
LL.print()

        




