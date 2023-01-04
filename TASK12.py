dict_1 = {'A': [1, 2, 3], 'b': ['1', '2'], "c": [4, 5, 6, 7]}
ctr = 0

for i in dict_1.values():
    for k in i:
        ctr += 1
    
print(ctr)