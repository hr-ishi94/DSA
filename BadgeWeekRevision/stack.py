stack =[]

def push():
    num=int(input("Enter the number: "))
    stack.append(num)
    print("new stack:",stack)
    return 

def pop():
    num = stack.pop(0)
    print(num," is popped out! ")
    return 

def peek():
    if stack:
        print("stack head is:",stack[-1])
    else:
        print("Stack is empty!")
    return

while True:
    print("Enter your choice: 1.push 2.pop 3.peek...")
    choice=int(input())
    if choice == 1:
        push()
    elif choice == 2:
        pop()
    elif choice == 3:
        peek()
    else:
        print("enter valid choice...!")