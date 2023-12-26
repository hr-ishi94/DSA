def heapify(arr,n,i):
    largest=i
    lchild=2*i+1
    rchild=2*i+2

    if lchild<n and arr[lchild]>arr[largest]:
        largest=lchild
    if rchild<n and arr[rchild]>arr[largest]:
        largest=rchild
    
    if largest!=i:
        arr[i],arr[largest]=arr[largest],arr[i]
        heapify(arr,n,largest)

def heap_sort(arr):
    n=len(arr)
    for i in range(n//2-1,-1,-1):
        heapify(arr,n,i)

    for i in range(n-1,0,-1):
        arr[i],arr[0]=arr[0],arr[i]
        heapify(arr,i,0)

arr=[23,45,6,43,23,12,2,3,4,75]
heap_sort(arr)
print('sorted array: ',arr)

