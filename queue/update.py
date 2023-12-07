arr=[12,23,45,65,43,34,56,3,2,2,43]
def update(num,replace):
    for i in range(len(arr)):
        if arr[i]==num:
            arr[i]=replace
            num=None
update(43,0)
print(arr)            
