def sort(arr):
    n=len(arr)

    for i in range(1,n):
        key=arr[i]
        j=i-1
        while j>=0 and key<arr[j]:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key

arr=[10,24,65,33,65,22,12,3232,3545346,56756867867,343,1]      
sort(arr)
print(arr)   