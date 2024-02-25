arr=[1,2,3,4,5,6,7,8,9]
n=23
k=7
def search(arr,n,k):
    low=0
    up=len(arr)-1
    while low<=up:
        mid=low+(up-low)//2

        if arr[mid]==n:
            arr[mid]=k
            print(arr)
            return
        else:
            if mid<n:
                low=mid
            else:
                up=mid
    return 

search(arr,n,k)            

