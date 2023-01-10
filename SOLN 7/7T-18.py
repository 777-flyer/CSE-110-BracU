def div_sum (f_range,l_range,f_divisor,s_divisor):
    
    sum = 0
    
    for i in range (f_range,l_range):
        
        if i % f_divisor == 0 and i % s_divisor == 0:
            continue
        
        elif i % f_divisor == 0 or i % s_divisor == 0:
            sum += i
            
    return sum

user_start = int(input("Sir,Please enter the first range please: "))
user_end = int(input("Sir,Please enter the second range please: "))

div1 = int(input("Sir,Please enter the first divisor please: "))
div2 = int(input("Sir,Please enter the second divisor please: "))

print(div_sum(user_start,user_end,div1,div2))