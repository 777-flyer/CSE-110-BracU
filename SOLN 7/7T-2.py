def fibonacci (x):
    num = 0
    num_1 = 1
    for i in range(x+1):
        if i == 0:
            print(num, end = " ")
        elif i == 1:
            print(num_1, end = " ")
        else:
            fibo = num + num_1
            num = num_1
            num_1 = fibo
            if fibo <= x:
                print(fibo, end = " ")
                
fibonacci(int(input("Sir,Please enter the range: ")))