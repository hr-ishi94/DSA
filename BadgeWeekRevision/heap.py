import heapq

arr = []

heapq.heappush(arr,56)
heapq.heappush(arr,1)
heapq.heappush(arr,3)
heapq.heappush(arr,6)
heapq.heappush(arr,19)
heapq.heappush(arr,22)

heapq.heappop(arr)
heapq.heappushpop(arr,22)
heapq.heappushpop(arr,25)

arr1= [1000,121212,3,4,5,6,3332,23,452435234,52523,523454454,5464]
heapq.heapify(arr1)

print(arr)
print(arr1)