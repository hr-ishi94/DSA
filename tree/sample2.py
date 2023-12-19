def heapify(arr,n,i):
    larg=i
    lchild=2*i+1
    rchild=2*i+2

    if lchild<n and arr[lchild]>arr[larg]:
        larg=lchild

    if rchild<n and arr[rchild]>arr[larg]:
        larg=rchild

    if larg!=i:
        arr[i],arr[larg]=arr[larg],arr[i]
        heapify(arr,n,larg)

def heap_sort(arr):
    n=len(arr)

    for i in range(n//2-1,-1,-1):
        heapify(arr,n,i)
    
    for i in range(n-1,-1,-1):
        arr[0],arr[i]=arr[i],arr[0]
    
        heapify(arr,i,0)

arr = [12, 11, 13, 5, 6, 7]
heap_sort(arr)
print("Sorted array:", arr)