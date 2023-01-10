def calender (user):
    remaining = user
    years = remaining // 365
    remaining = remaining % 365
    months = remaining // 30
    remaining = remaining % 30
    days = remaining 
    
    print("{} years, ".format(years),end = "")
    print("{} months and".format(months),end = " ")
    print("{} days".format(days))
    
calender(int(input("Sir,Please enter the number of days: ")))