class Node :
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.front = None
        self.rear = None
    
    def isEmpty(self):
        return self.front is None
    
    def enqueue(self,data):
        new_node = Node(data)
        if self.isEmpty():
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        
    def dequeue(self):
        if self.isEmpty():
            print("Empty linkedlist!")
            return None
        else:
            temp = self.front.data
            self.front = self.front.next
            return temp
        
    def head(self):
        if self.isEmpty():
            print("Empty linked list")
            return
        else:
            print("Head of the queue: ", self.front.data)
            return
        
    def get_rear(self):
        if not self.rear:
            print("Empty linked list!")
            return
        else:
            print("Rear of the queue: ",self.rear.data)
            return

    def printLL(self):
        n = self.front
        while n :
            print(n.data, "-->",end=" ")
            n = n.next
        return 
    
LL= LinkedList()
LL.enqueue(10)
LL.enqueue(20)
LL.enqueue(30)
LL.enqueue(40)
LL.enqueue(50)
LL.get_rear()
print(LL.dequeue())
print(LL.dequeue())
LL.head()
print(LL.dequeue())
print(LL.dequeue())
LL.printLL()
