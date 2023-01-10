def show_palindrome (user):
    for count in range (1,user):
        print(count, end = "")
    for rev_count in range (user,0,-1):
        print(rev_count, end = "")
    print('')
    
#function call
show_palindrome(6)