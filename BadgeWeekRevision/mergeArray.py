arr = [28, 26, 54, 3, 11]

print("Before sorting : ",arr)

def merge_sort (arr):
    if len(arr)<=1:
        return arr
    
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left,right)

def merge(left,right):
    merged= []
    i=j=0

    while len(left)>i and len(right)>j:
        if left[i]<right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged

print("After sorting : ",merge_sort(arr))
   