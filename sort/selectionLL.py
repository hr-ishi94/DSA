class Node:
    def __init__ (self, data):
        self.data = data
        self.ref = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node
    
    def printLL(self):
        n = self.head
        while n:
            print(n.data, '-->', end='')
            n = n.ref
    
    def selectionsort(self):
        if not self.head or not self.head.ref:
            return self.head

        curr = self.head
        while curr:
            min_node = self.find_min()  # Removed curr argument here
            self.swap(curr, min_node)
            curr = curr.ref
    
    def find_min(self):
        min_node = self.head
        curr = self.head.ref

        while curr:
            if curr.data < min_node.data:
                min_node = curr
            curr = curr.ref
        return min_node
    
    def swap(self, node1, node2):
        temp = node1.data
        node1.data = node2.data
        node2.data = temp

# Example usage:
if __name__ == "__main__":
    LL = LinkedList()
    LL.push(11)                    
    LL.push(12)                    
    LL.push(13)                    
    LL.push(14)                    
    LL.push(15)                    
    LL.push(16)
    LL.selectionsort()
    LL.printLL()
