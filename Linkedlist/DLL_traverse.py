class Node:
    def __init__(self,data):
        self.data= data
        self.nref=None
        self.pref=None

class DoubleLinkedList:
    def __init__(self):
        self.head=None
    
    def printDLL(self):
        if self.head is None:
            print('Linked list is empty!')
        else:
            n=self.head
            while n.nref is not None:
                print(n.data,end=' ')
                n=n.nref

    def printDLL_reverse(self):
        if self.head is None:
            print('Linked list is empty!')
        else:
            n=self.head
            while n is not None:
                n=n.nref
            while n is not None:
                print(n.data)
                n=n.pref

DLL=DoubleLinkedList()
DLL.printDLL()
DLL.printDLL_reverse()



    
