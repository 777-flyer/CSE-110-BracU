list_1 = [("a", 1), ("b", 2), ("a", 3), ("b", 1), ("a", 2), ("c", 1)]
new_dict = {}
for i in list_1:
    key = i[0]
    value = i[1]
    
    if key in new_dict.keys():
        new_dict[key].append(value)
    else:
        new_dict[key] = [value]
        
print(new_dict)
        