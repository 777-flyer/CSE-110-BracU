given_tuple = (10,8,5,2,10,15,10,8,5,8,8,2)
n = int(input("Enter a number: "))
length = len(given_tuple)
c = 0
for i in range(length):
    if given_tuple[i] == n :
        c += 1 
        
print(f"{n} appeared {c} times")