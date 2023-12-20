import heapq

arr=[12,34,654,76,34,23,4,5]
heapq.heapify(arr)

heapq.heappush(arr,13)
heapq.heappop(arr)
heapq.heappushpop(arr,11)
heapq.heapreplace(arr,1)
print(heapq.nsmallest(5,arr))
print(heapq.nlargest(5,arr))
print(arr)


#Priority Queue
list3=[[31,'Hrishi'],[12,'Arathy'],[53,'Ammu'],[1,'mohanlal']]
heapq.heapify(list3)
for i in list3:
    print(i)