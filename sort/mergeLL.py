class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def mid(head):
    slow=head
    fast=head.next

    while fast and fast.next:
        slow=slow.next
        fast=fast.next.next

    return slow

def merge(head):
    if not head or not head.next:
        return head
    
    left=head
    right=mid(head)
    temp=right.next
    right.next=None
    right=temp

    left=merge(left)
    right=merge(right)

    return sort(left,right)

def sort(left,right):
    tail=dummy=Node(0)

    while left and right:
        if left.data<right.data:
            tail.next=left
            left=left.next
        else:
            tail.next=right
            right=right.next
        tail=tail.next
    
    while left:
        tail.next=left
    while right:
        tail.next=right

def printLL(head):
    while head:
        print(head.data,end=' ')        
        head=head.next

head = Node(3)
head.next = Node(1)
head.next.next = Node(4)
head.next.next.next = Node(2)
head.next.next.next.next = Node(2)

printLL(head)
merge(head)
printLL(head)

