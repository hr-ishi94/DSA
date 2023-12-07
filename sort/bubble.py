def sort(arr):
    for i in range(len(arr)):
        for j in range(0,len(arr)-i-1):
            if arr[j+1]<arr[j]:
                arr[j],arr[j+1]=arr[j+1],arr[j]

arr=[10,24,65,33,65,22,12,3232,3545346,56756867867,343,1]      
sort(arr)
print(arr)          
                