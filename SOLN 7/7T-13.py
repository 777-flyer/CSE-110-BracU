def calculator (operator,first_operand, second_operand):
    
    
    if operator == "+":
        return first_operand + second_operand
    elif operator == "-":
        return first_operand - second_operand
    elif operator == "*":
        return first_operand * second_operand
    elif operator == "/":
        return first_operand / second_operand
    
operator = input("Sir,Please enter the operator: ")
first_operand = float(input("Sir,Please enter the first operand: "))
second_operand = float(input("Sir,Please enter the second operand: "))

print(calculator(operator,first_operand,second_operand))