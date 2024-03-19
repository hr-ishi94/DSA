class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def arr_to_LinkedList(self,arr):
        new_node = Node(arr[0])
        self.head = new_node

        n = self.head 
        for i in range(1,len(arr)):
            new_node = Node(arr[i])
            n.next = new_node
            n = new_node

        return
    def printLL(self):
        n = self.head
        while n:
            print(n.data,"---> ",end="")
            n = n.next
        print("")
        print("Head of the linked list is :", self.head.data)
        

arr= [1,12,2,3,4,5,6,7,8]
LL = LinkedList()
LL.arr_to_LinkedList(arr)
LL.printLL()




