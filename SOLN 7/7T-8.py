def show_palindromic_triangle (user):
    for row in range (1, user + 1):
        for space in range (1, (user - row) + 1):
            print(" ", end = " ")
        for numbers in range (1,row):
            print(numbers, end = " ")
        for numbers in range (row, 0, -1):
            print(numbers, end = " ")
        print('')
        
#function call

show_palindromic_triangle(5)