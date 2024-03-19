class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_begin(self,data):
        new_node =Node(data)
        new_node.next = self.head
        self.head = new_node

    def printLL(self):
        if not self.head:
            print("Empty linked list!")
            return
        n = self.head
        while n:
            print(n.data,"---> ", end=" ")
            n = n.next

    def reverse_linked_list(self):
        if not self.head:
            print("Empty linked list!")
            return
        prev = None
        curr = self.head
        
        while curr:
            new_node = curr.next
            curr.next = prev
            prev = curr
            curr = new_node

        while prev:
            print(prev.data,"---> " , end= " ")
            prev = prev.next

    def middle_node_linked_list(self):
        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        print("Middle node is :",slow.data)

LL = LinkedList()
# LL.add_begin(60)
LL.add_begin(50)
LL.add_begin(40)
LL.add_begin(30)
LL.add_begin(20)
LL.add_begin(10)
print("Before reversing: ")
LL.printLL()
print("")
LL.middle_node_linked_list()
print("After reversing: ")
LL.reverse_linked_list()