#----------------------------------------------
#task---01

numone = int(input("Please enter the first number: "))
numtwo = int(input("Please enter the second number: "))
sum = numone + numtwo
product = numone * numtwo
difference = numone - numtwo
print("Sum={}".format(sum))
print("Product={}".format(product))
print("Difference={}".format(difference))

#----------------------------------------------
#task---02

import math
rad = float(input("Sir,Please enter the radius: "))
circum = 2*math.pi*rad
area = math.pi*rad**2
print("Area is",area)
print("Circumference is",circum)

#----------------------------------------------
#task---03

first = int(input("Please enter the first number: "))
second = int(input("Please enter the second number: "))
if first > second :
  print("First is greater")
elif second > first:
  print("Second is greater")  
else:
  print("The numbers are equal")  
  
#----------------------------------------------
#task---04

first = int(input("Please enter the first number: "))
second = int(input("Please enter the second number: "))
if first > second :
  print(first - second)
else: 
  print(second - first)
  
#----------------------------------------------
#task---05

var = int(input("Please enter a number: "))
if var%2 == 0:
  print("The number is even")
else:
  print("The number is odd")

#----------------------------------------------
#task---06

var = int(input("Please enter a number: "))
if var%2 == 0:
  print(var)
elif var%5 == 0:
  print(var)  
else:
  print("Not a multiple of 2 OR 5")  
  
#----------------------------------------------
#task---07

var = int(input("Please enter a number: "))
if var%2 == 0 and var%5 == 0:
  print("Multiple of 2 and 5 both")
elif var%2 == 0:
  print(var)
elif var%5 == 0:
  print(var)
else:
  print("Not a multiple we want")  
  
#----------------------------------------------
#task---08

var = int(input("Please enter a number: "))
if var%2 == 0 and var%5 == 0:
  print(var)
else:
  print("Not multiple of 2 and 5 both")  
  
#----------------------------------------------
#task---09

var = int(input("Sir,Please do enter the number of seconds: "))
hrs = var // 3600
min1 = var % 3600
min2 = min1 // 60
second = min1 % 60
print("Hours: {} Minutes: {} Seconds: {}".format(hrs,min2,second))

#----------------------------------------------
#task---10

var = int(input("Sir,Please do enter the number of hours you have worked: "))
more = 8000+(var-40)*300
if var<0:
  print("Hour cannot be negative")
elif var>168:
  print("Impossible to work more than 168 hours weekly")
elif var<=40:
  print(var*200)
elif var>40:
  print(more)  
else:
  print("Please enter a valid input")
  
#----------------------------------------------
#task---11

var = int(input("Please enter the value of S: "))
less100 = 3000-125*var**2
more100 = 12000/(4+var**2/14900)
if var<100:
  print(less100)
elif var>=100:
  print(more100) 
else:
  print("Please enter a valid number")
  
#----------------------------------------------
#task---12


var = int(input("Sir,Please do enter the time: "))
if var>=0 and var<=23:
  if var>=4 and var<=6:
    print("Breakfast")
  elif var>=12 and var<=13:
    print("Lunch")
  elif var>=16 and var<=17:
    print("Snacks")
  elif var>=19 and var<=20:
    print("Dinner")
  else:
    print("Patience is a virtue")
else:
  print("Wrong time")
  
#----------------------------------------------
#task---13


var = int(input("Please enter the mark you got: "))


if var>=0 and var<=100:
  
  if var>=90 and var<=100:
    print("A")
  elif var>=80 and var<=89:
    print("B")
  elif var>=70 and var<=79:
    print("C")                                # follow the indentations carefully
  elif var>=60 and var<=69: 
    print("D")
  elif var>=50 and var<=59: 
    print("E")
  else:
    print("F")
    
else:
  print("Please enter a valid input")
  
  #----------------------------------------------
#task---14

var = int(input("Enter the distance in meters: "))
var2 = int(input("Enter the time in seconds: "))

km = var/1000
hr = var2/3600
velo = km/hr

print("{} km/h".format(velo))

if velo<60:
  print("Too slow. Needs more changes.")
elif velo>=60 and velo<=90:
  print("Velocity is okay. The car is ready!")  
else:
  print("Too fast. Only a few changes should suffice.")
  
  
#----------------------------------------------
#task---15

cg = float(input("Enter your CGPA here: "))
cred = int(input("Total credits done: "))
if cred>=30:
  if cg>=3.80 and cg<=3.89:
    print("The student is eligible for a waiver of 25 percent")
  elif cg>=3.90 and cg<=3.94:
    print("The student is eligible for a waiver of 50 percent") 
  elif cg>=3.95 and cg<=3.99:
    print("The student is eligible for a waiver of 75 percent")  
  elif cg == 4.00:
    print("The student is eligible for a waiver of 100 percent")  
  else:
    print("The student is not eligible for a waiver")  
else:
  print("The student is not eligible for a waiver")  