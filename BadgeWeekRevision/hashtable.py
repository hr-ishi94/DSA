dict = {1:'Hrishi',2:'prasad',3:'Hrishikesh'}

print(type(dict))
print(dict)

print(dict.values())
print(dict.keys())

print(dict.get(1))
print(dict.get(2))
print(dict.get(3))

for x,y in dict.items():
    print("key: ",x)
    print("Values: ",y)

dict['4'] = 'arathy'
dict['5'] = 'Av'
print(dict)


arr1 = [1,2,3,4,5,6]
arr2 = [8,9,10,11,12,13]

