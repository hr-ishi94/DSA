arr=[3,4,4,57,8,433,2]

def middle(arr):
     if len(arr)>1:
        mid=len(arr)//2

        left=arr[:mid]
        right=arr[mid:]

        middle(left)
        middle(right)

        sort(arr,left,right)

def sort(arr,left,right):
    i=j=k=0

    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            arr[k]=left[i]
            i+=1
        else:
            arr[k]=right[j]
            j+=1
        k+=1

    while i<len(left):
        arr[k]=left[i]
        i+=1
        k+=1
            
    while j<len(right):
        arr[k]=right[j]
        j+=1
        k+=1

print(arr)
middle(arr)
print(arr)        

