def rem_duplicate (user):
    user_list = list(user)
    new_list = []
    for i in user_list:
        if i not in new_list:
            new_list.append(i)
    tup = tuple(new_list)
    return tup

#function call

print(rem_duplicate((1,1,1,2,3,4,5,6,6,6,6,4,0,0,0)))
    