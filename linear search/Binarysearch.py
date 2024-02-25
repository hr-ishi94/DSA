arr=[21,34,23,76,87,11,32,43]
arr.sort()
print(arr)
n=76
pos =-1
def binarySearch(arr,n):
    low=0
    up=len(arr)-1

    while low<=up:
        mid=low+(up-low)//2
        if arr[mid]==n:
            globals() ['pos']=mid
            return True
        else:
            if arr[mid]<n:
                low=mid
            else:
                up=mid
    return False

if binarySearch(arr,n):
    print('found at ', pos+1)
else:
    print('Not Found!')
