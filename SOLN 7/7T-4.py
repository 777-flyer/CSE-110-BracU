def upper_lower(string):
    
    up = 0
    low = 0
    
    for chr in string:
        if ord("A") <= ord(chr) <= ord("Z"):
            up += 1
        elif ord("a") <= ord(chr) <= ord("z"):
            low += 1
    print("No. of Upper characters : {} ".format(up))
    print("No. of lower characters : {}".format(low))
    
upper_lower("The quick Sand Man")