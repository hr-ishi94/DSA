def merge_dictionaries(dict1, dict2):
    for x in dict1:
        if x in dict2:
            dict1[x]=dict2[x]
    dict1.update(dict2)    
    return dict1 
# Example usage:
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
merged_dict = merge_dictionaries(dict1, dict2)
print(merged_dict)
