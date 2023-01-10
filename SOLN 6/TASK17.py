my_dictionary = {'c1':'Red', 'c2':'Green', 'c3':None, 'd4':'Blue', 'a5':None}
new_dict = {}
for k,v in my_dictionary.items():
    if v == None:
        continue
    else:
        new_dict[k] = v
        
print(new_dict)