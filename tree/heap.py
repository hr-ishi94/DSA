import heapq
list1=[]

heapq.heappush(list1,50)
heapq.heappush(list1,30)
heapq.heappush(list1,20)
heapq.heappush(list1,5)
heapq.heappush(list1,10)
print(list1)
heapq.heappop(list1)
heapq.heappushpop(list1,12)
print(list1)

list2=[123,24,56,76,34,2,2535,67]

heapq.heapify(list2)
print(list2)
print(heapq.nsmallest(3,list1))
print(heapq.nlargest(3,list2))

list3=[(1,'hrishi'),(7,'prasad'),(3,'hrishikesh')]
heapq.heapify(list3)
print(list3)
for i in range(len(list3)):
    print(heapq.heappop(list3))