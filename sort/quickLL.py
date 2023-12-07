class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def partition(start, end):
    pivot_value = start.data
    pivot = start
    current = start.next

    while current :
        if current.data < pivot_value:
            pivot = pivot.next
            current.data, pivot.data = pivot.data, current.data
        current = current.next

    start.data, pivot.data = pivot.data, start.data
    return pivot

def quicksort(start, end=None):
    if start and start != end:
        pivot = partition(start, end)
        quicksort(start, pivot)
        quicksort(pivot.next, end)

def print_list(node):
    while node:
        print(node.data, end=" ")
        node = node.next
    print()

# Example usage:
# Create a linked list
head = Node(3)
head.next = Node(1)
head.next.next = Node(4)
head.next.next.next = Node(2)
head.next.next.next.next = Node(2)

# Find the end of the linked list
end = head
while end.next:
    end = end.next

print("Original Linked List:")
print_list(head)

# Call quicksort with the correct end parameter
quicksort(head, end)

print("Sorted Linked List:")
print_list(head)
