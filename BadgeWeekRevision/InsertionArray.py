arr = [28,26,54,3,11]

print("Before sorting : ", arr)

for i in range(len(arr)):

    key = arr[i]
    j =  i-1

    while j>=0 and key<arr[j]:
        arr[j+1] = arr[j]
        j -= 1
    arr[j+1] = key

print("After sorting : ",arr)