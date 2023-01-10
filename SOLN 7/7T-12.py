#task12
def max_two (user):
    fresh_list = user 
    new_list = [] 
    removed = 0
    for i in fresh_list:
        amount = 0
           
        for j in fresh_list:
            if i == j:
                amount+=1
       
        if amount>2 and i not in new_list:
            new_list.append(i)
            new_list.append(i)
            removed += (amount-2)
        elif amount==2 and i not in new_list:
            new_list.append(i)
            new_list.append(i)
        elif i not in new_list:
             new_list.append(i)
    print("Removed:",removed)
    return new_list


print(max_two([10, 10, 10, 15, 15, 15, 20]))

    