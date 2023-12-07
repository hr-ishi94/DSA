def merge_sort(arr):
    if len(arr)>1:
        mid=len(arr)//2

        left=arr[:mid]
        right=arr[mid:]

        merge_sort(left)
        merge_sort(right)

        merge(arr,left,right)

def merge(arr,left,right):
    i=j=k=0

    while len(left)>i and len(right)>j:
        if left[i]<right[j]:
            arr[k]=left[i]
            i+=1
        else:
            arr[k]=right[j]
            j+=1
        k+=1
    
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1

arr=[5,6,7,3,2,8,23,4]

merge_sort(arr)
print(arr)