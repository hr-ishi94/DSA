arr=[12,32,43,54,23,2,121,21,1,32,4]
list1=[]
for i in range(len(arr)):
    list1.append(arr[i])
    print(list1)

print()
print()
for i in range(len(list1)):
    list1.pop(0) 
    print(list1)
