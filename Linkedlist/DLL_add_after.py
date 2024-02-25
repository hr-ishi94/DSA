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
            while n is not None:
                print(n.data,'-->',end=' ')
                n=n.nref

    def printDLL_reverse(self):
        print()
        if self.head is None:
            print('Linked list is empty!')
        else:
            n=self.head
            while n.nref is not None:
                n=n.nref
            while n is not None:
                print(n.data,'-->',end=' ')
                n=n.pref

    def insert(self,data):
        if self.head is None:
            new_node=Node(data)
            self.head=new_node
        else:
            print('linked list is not empty!')

    def insert_begin(self,data):
        n=self.head
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            new_node.nref=self.head
            self.head.pref=new_node
            self.head=new_node

    def insert_end(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            n=self.head
            while n.nref is not None:
                n=n.nref
           
            n.nref=new_node
            new_node.pref=n

    def add_after(self,data,x):
        new_node=Node(data)
        if self.head is None:
            print('Linked list is empty!')
            return
        else:
            n=self.head
            while n.nref is None:
                if n.data==x:
                    break
                n=n.nref
            
            if n is None:
                print('Node not found!!')
            else:
                new_node.nref=n.nref
                new_node.pref=n
                if n.nref is not None:
                    n.nref.pref=new_node
                n.nref=new_node
                




DLL=DoubleLinkedList()
DLL.insert(10)
DLL.insert_begin(100)
DLL.insert_end(20)
DLL.insert_end(150)
DLL.add_after(55,10)
DLL.printDLL()
DLL.printDLL_reverse()



    
