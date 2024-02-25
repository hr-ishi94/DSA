arr=[10,5,4,3,7,8,32]
pos=-1
def search(list1,n):
    i=0

    while i<len(list1):
        if n == list1[i]:
            globals()['pos']=i
            return True
        i+=1
    return False

if search(arr,7):
    print('Found at',pos+1)
else:
    print('not found')