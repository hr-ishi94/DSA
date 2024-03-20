from collections import deque

arr = [1,2,3,4,5,6,7]

que = deque()

def enqueue(arr):
    for i in range(len(arr)):
        que.append(arr[i])

def dequeue(arr):
    temp = arr.popleft()
    return temp

def head(arr):
    return arr[0]

enqueue(arr)
print(arr)
print("Result to be removed:  ",dequeue(que))
print("Head of the queue: ",head(que))