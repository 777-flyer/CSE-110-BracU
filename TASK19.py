list_a = [(20, 'Sad'), (31, 'Sad'), (88, 'NotSad'), (27, 'NotSad')]
new_dict = {}

for i in range (len(list_a)):
    key = list_a[i][1]
    value = []
    
    for j in range (len(list_a)):
        
        if key == list_a[j][1]:
            value.append(list_a[j])
            
    new_dict [key] = value
    
print(new_dict)