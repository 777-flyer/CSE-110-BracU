import math

def area_circumference_generator (user):
    radius = user
    list_circle = []
    circumference = 2*math.pi*radius
    area = math.pi*radius**2
    list_circle.append(area)
    list_circle.append(circumference)
    tuple_a = tuple(list_circle)
    out = ('Area of the circle is {} and circumference is {}'.format(tuple_a[0],tuple_a[1]))
    return tuple_a,out

final = area_circumference_generator(float(input("Sir,Please enter the radius: ")))
print(final[0])
print(final[1])