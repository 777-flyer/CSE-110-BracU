dict1 = {'Harry':15, 'Draco':8, 'Nevil':19}
dict2 = {'Ginie':18, 'Luna': 14}

new_dict = {}

for i,j in dict1.items():
    new_dict[i] = j
for k,m in dict2.items():
    new_dict[k] = m
    
print(new_dict)