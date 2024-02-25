def binary_search(arr, target, low=None, high=None):
    if low is None and high is None:
        low, high = 0, len(arr) - 1

    mid = low + (high - low) // 2

    if target == arr[mid]:
        return mid+1
    elif target < arr[mid]:
        return binary_search(arr, target, low, mid - 1)
    else:
        return binary_search(arr, target, mid + 1, high)

arr = [1, 2, 3, 4, 5, 6, 7]
result = binary_search(arr, 7)
print(result)
