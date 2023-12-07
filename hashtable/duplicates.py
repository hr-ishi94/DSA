def remove_duplicates(dict1):
    res={key:value for key,value in dict1.items() if list(dict1.values()).count(value)==2}
    return res

dict1={'a': 1, 'b': 2, 'c': 3, 'd': 2, 'e': 1}
res=remove_duplicates(dict1)
print(res)