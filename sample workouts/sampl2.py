class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None

class stack:
    def __init__(self):
        self.top=None

    def push(self,data):
        new_node=Node(data)
        new_node.ref=self.top
        self.top=new_node

    def pop(self):
        if self.top is None:
            print('EMPTY!')
        
        self.top=self.top.ref
            


    def printLL(self):
        n=self.top
        while n:
            print(n.data,end=' ')
            n=n.ref


class queue:
    def __init__(self):
        self.front=None
        self.rear=None
    
    def enqueue(self,data):
        new_node=Node(data)
        if self.is_empty():
            self.front=self.rear=new_node
        else:
            self.rear.ref=new_node
            self.rear=new_node

    def is_empty(self):
        return self.front is None

    def dequeue(self):
        if not self.front :
            return None
        else:
            self.front=self.front.ref
            if self.front is None:
                self.rear= None

    def printLL(self):
        n=self.rear
        while n:
            print(n.data,end=' ')
            n=n.ref






# stack=stack()

# stack.push(12)
# stack.push(14)
# stack.push(13)
# stack.push(15)
# stack.pop()
# stack.pop()
# stack.pop()
# stack.printLL()      


queue=queue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.enqueue(40)
queue.enqueue(50)
# queue.dequeue()
queue.printLL()
