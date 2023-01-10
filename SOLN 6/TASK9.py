exam_marks = {'Cierra Vega': 175, 'Alden Cantrell': 200, 'Kierra Gentry': 165, 'Pierre Cox': 190}
user = int(input("Sir,Please enter the number: "))
up_dict = {}
for key,value in exam_marks.items():
    if exam_marks[key] >= user:
        up_dict[key] = value
        
print(up_dict)