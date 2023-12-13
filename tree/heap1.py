class MinHeap:
    def __init__(self):
        self.heap = []

    def push(self, value):
        self.heap.append(value)
        self._heapify_up()

    def pop(self):
        if len(self.heap) > 1:
            self._swap(0, len(self.heap) - 1)
            min_val = self.heap.pop()
            self._heapify_down()
        elif len(self.heap) == 1:
            min_val = self.heap.pop()
        else:
            raise IndexError("pop from an empty heap")
        return min_val

    def peek(self):
        if self.heap:
            return self.heap[0]
        else:
            raise IndexError("peek from an empty heap")

    def _heapify_up(self):
        index = len(self.heap) - 1
        while index > 0:
            parent_index = (index - 1) // 2
            if self.heap[index] < self.heap[parent_index]:
                self._swap(index, parent_index)
                index = parent_index
            else:
                break

    def _heapify_down(self):
        index = 0
        while True:
            left_child_index = 2 * index + 1
            right_child_index = 2 * index + 2
            smallest = index

            if left_child_index < len(self.heap) and self.heap[left_child_index] < self.heap[smallest]:
                smallest = left_child_index

            if right_child_index < len(self.heap) and self.heap[right_child_index] < self.heap[smallest]:
                smallest = right_child_index

            if smallest != index:
                self._swap(index, smallest)
                index = smallest
            else:
                break

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

# Example usage:
min_heap = MinHeap()
min_heap.push(3)
min_heap.push(1)
min_heap.push(4)
min_heap.push(2)

print("Min heap:", min_heap.heap)

print("Peek:", min_heap.peek())

print("Pop:", min_heap.pop())
print("Min heap after pop:", min_heap.heap)
