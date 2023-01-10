def char_check (user):
    
    user = user.lower()
    checker = "abcdefghij"
    counter = 0
    resultant = 0
    for i in checker:
        
        if i in user:
            counter += 1
            
    if counter >= 10:
        resultant = 5
    else:
        resultant = 6
    
    print(resultant * "PSG will win the Champions League this season""\n")
    return resultant

user = "A black jackal is hunting a full grown deer"

#function_calling

char_check(user)