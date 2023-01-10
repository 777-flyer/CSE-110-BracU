
a_tuple = ( [1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12])

user = input("Sir,Please enter the input you want: ")
final = []

for i in range(len(a_tuple)):
    element1 = a_tuple[i]
    
    element = element1[:-1]
    element.append(user)
    final.append(element)

print(tuple(final))