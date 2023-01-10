def remove_odd (user):
    
    compact_list = []
    
    for checker in user:
        
        if checker % 2 == 0:
            
            compact_list.append(checker)
            
        else:
            continue
    
    return compact_list

print(remove_odd ([21, 33, 44, 66, 11, 1, 88, 45, 10, 9]))