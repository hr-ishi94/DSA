class Node:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def add_begin(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        return
    
    def add_after(self,data,x):
        if not self.head:
            print(x, " node not found!")
            return
        new_node = Node(data)
        if self.head.data == x:
            new_node.next = self.head.next
            new_node.prev = self.head
            self.head.next = new_node
        else:    
            n = self.head
            while n:
                if n.data == x:
                    break
                n = n.next
            if not n:
                print("Node not found!")
                return
            new_node.next = n.next
            new_node.prev = n
            n.next = new_node
            return

    def PrintList(self):
        if not self.head:
            print("Empty list!")
            return
        
        n = self.head
        while n:
            print(n.data,"-->", end = "")
            n = n.next

LL = LinkedList()
# LL.add_begin(10)
# LL.add_begin(20)
LL.add_after(25,20)
LL.PrintList()