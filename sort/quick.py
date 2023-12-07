def sort(arr):
    n=len(arr)

    if n<=1:
        return arr
    else:
        pivot=arr[0]
        less=[x for x in arr[1:] if x<=pivot]
        larg=[x for x in arr[1:] if x>pivot]
        return sort(less)+[pivot]+sort(larg)
    
arr=[9,8,4,5,10,17,21,6]
ass=sort(arr)
print(ass)

