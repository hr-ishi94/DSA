arr = [28,26,54,3,11]

print("Array before sorting : ",arr)

for i in range(len(arr)):

    min_index= i

    for j in range(i+1,len(arr)):
        if arr[j]<arr[min_index]:
            min_index = j
    
    arr[i],arr[min_index] = arr[min_index],arr[i]

print("Array after sorting : ",arr)