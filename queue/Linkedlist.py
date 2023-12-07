class Node:
    def __init__(self,data) :
        self.data=data
        self.ref=None

class QueueList:
    def __init__(self) :
        self.front= None
        self.rear=None

    def enqueue(self,data):
        new_node= Node(data)
        if self.is_empty():
            self.front=self.rear=new_node
        else:
            self.rear.ref=new_node
            self.rear=new_node

    def dequeue(self):
        if self.is_empty():
            return None
        else:
            dq_data=self.front.data
            self.front=self.front.ref
            if self.front is None:
                self.rear= None
            return dq_data
    def front(self):
        return self.front.data if self.front else None
    
    def is_empty(self):
        return self.front is None
    
    def printLL(self):
        n=self.front
       
        while n:
            print(n.data,'-->',end='')
            n=n.ref


LL=QueueList()
LL.enqueue(12)
LL.enqueue(13)
LL.enqueue(14)
LL.enqueue(15)
LL.enqueue(16)
LL.dequeue()
LL.dequeue()
LL.dequeue()
LL.dequeue()
LL.dequeue()
      
     
LL.printLL()