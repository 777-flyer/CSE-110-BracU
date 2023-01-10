def calculate_tax (age,salary,job):
    tax = 0
    if age < 18 or job == "president":
        tax = float(0)
    elif salary < 10000:
        tax = float(0)
    elif 10000<=salary<=20000:
        tax = ((salary*5)/100)
    elif salary > 20000:
        tax = ((salary*10)/100)
        
    return tax
Age = int(input("Sir,Please enter your age: "))
Salary = int(input("Sir,Please enter your salary: "))
Job = input("Sir,Please enter your job: ")

print(calculate_tax(Age,Salary,Job))