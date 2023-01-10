def splitting_money (amount):
    
    note_types = [500,100,50,20,10,5,2,1]
    notes = ""
    note_count = 0
    
    for count in note_types:
        
        note_count = amount // count
        
        if note_count == 0:
            break
        elif note_count == 1:
            notes += f'{count} Taka : {note_count} note' + "\n"
        elif note_count > 1:
            notes += f'{count} Taka : {note_count} note(s)' + "\n"
            
        amount = amount % count
        
    return notes

user = int(input("Sir,Please enter the amount of money: "))

print(splitting_money(user))