dict_1 = {'a' : 6, 'b' : 7, 'c' : 9, 'd' : 8, 'e' : 11, 'f' : 12, 'g' : 13}
user = int(input("Sir,PLease enter the min point: "))
user_2 = int(input("Sir,PLease enter the max point: "))

new_dict = {}

for k,v in dict_1.items():
    if user<=dict_1[k]<user_2:
        new_dict[k] = v
    else:
        pass
print(new_dict)

