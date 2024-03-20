arr= [ 1,2,3,4,5,6,7,8 ]
stack = []

def push(arr):
    for i in arr:
        stack.append(i)
    return stack

def pop(arr):
    pop = arr.pop()
    return pop

def peek(arr):
    return arr[-1]

print(push(arr))
print(pop(arr))
print(pop(arr))
print(pop(arr))
print(pop(arr))
print(arr)
print(peek(arr))