arr = [16,72,33,23,65,24,22,11,74]
print("Before sorting: ",arr)
n = len(arr)
for i in range(n):
    for j in range(0, n-i-1):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1] = arr[j+1],arr[j]
        

print("After sorting: ",arr)