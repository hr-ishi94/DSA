arr = [1,2,4,332,553,232,2435,45,23]
tar = 332
# LINEAR SEARCH
for i in range(len(arr)):
    if arr[i] == tar:
        print("Found at ",i)

array = [4,5,6,7,8,9,10]
target = 4
# BINARY SEARCH
def binary_search(arr,tar):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = ( high + low )//2
        if arr[mid] == tar:
            return mid
        elif tar<arr[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return -1

print(binary_search(array,target))
