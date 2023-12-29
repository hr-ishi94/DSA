arr=[12, 11,13,5,6,8,9]

def heapify(arr,i,n):
    largest=i
    lchild=2*i+1
    rchild=2*i+2

    if lchild<n and arr[lchild]>arr[largest]:
        largest=lchild
    if rchild<n and arr[rchild]>arr[largest]:
        largest=rchild

    if largest!=i:
        arr[largest],arr[i]=arr[i],arr[largest]
        heapify(arr,largest,n)

def heap_sort(arr):
    n= len(arr)

    for i in range(n//2-1,-1,-1):
        heapify(arr,i,n)

    for i in range(n-1,0,-1):
        arr[0],arr[i]=arr[i],arr[0]
        heapify(arr,0,i)

heap_sort(arr)
print(arr)