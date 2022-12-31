#TASK1


print("(a)",end="")

i = 30
count = 0
while count<=5:
    if count == 5:
      i-=6
      print(i, end = "")
    else:
       i-=6
       print(i, end = ",")
    count = count+1

print("")


#TASK1.1


print("(b)", end = "")

i = -15
count = 0
while count<=6:
  if count == 6:
    i += 5
    print(i, end = "")
  else:
    i += 5
    print(i, end = ",")
  count += 1

print("")


#TASK1.3


print("(c)", end = "")

i = 9
count = 0
while count<=5:
  if count == 5:
    i += 9
    print(i, end = "")
  else:
    i += 9
    print(i, end = ",")
  count = count+1

print("")


#TASK1.4


print("(d)",end = "")

start = 18
while start<64:
  if start%2 == 0:
    print(start, end = ",")
  elif start%9 == 0 and 62<start<64:
    print(start*-1, end = "")
  else:
    print(start*-1, end = ",")
  start += 9  
  
#-------------------------------------------------------------------
#task2

fav_car = input("Your favourite car: ")
times = int(input("Enter the number of times: "))
counter = 1
while counter<=times:
    print(fav_car)
    counter += 1
#-------------------------------------------------------------------
#task3

var = 1
sum = 0
while var<=600:
  if var%7 == 0 and var%9 == 0:
    sum += var
  var += 1
print("The summation is:",sum) 
#-------------------------------------------------------------------
#task4

start = 1
sum = 0
while start<=600:
  if (start%7 == 0 and start%9 != 0) or (start%7 != 0 and start%9 == 0):
    sum += start
  start += 1
print("Total summation is:",sum)
#-------------------------------------------------------------------
#task5 

start = 10
while start<50:
  if start%2 != 0:
    print(start, end = " ")

  start += 1
#-------------------------------------------------------------------
#task6

y = int(input("Sir,Please enter your desired number: "))
sum = 0
counter = 1
while counter<=y:
  if counter%2 == 0:
    sum = sum - (counter*counter)
  else:
    sum = sum + (counter*counter)
  counter = counter + 1
print(sum)   
#-------------------------------------------------------------------
#task7

counter = 1

total = 0

times = 0

while counter<=10:
  user = int(input("Sir,Please enter your numbers: "))
  if user%2 == 1:
    total = total + user
    times = times + 1
  counter += 1
average = total/times
print("The total of the odd numbers is {} and their average is {}".format(total,average))    
#-------------------------------------------------------------------
#task8

user = int(input("Sir,Please enter a number: "))
sum = 0
counter = 0

while counter<=user:
  if counter%7 == 0:
      sum = sum+counter
  counter = counter+1

print(sum)      
#-------------------------------------------------------------------
#task9

sum = 0
counter = 0

while counter<5:
  user = int(input("Sir,Please enter your numbers: "))
  
  sum = user+sum

  print(sum)

  
  counter = counter + 1    
#-------------------------------------------------------------------
#task10

user = int(input("Sir,Please enter a number: "))

while user>0:
  remainder = user%10
  if remainder//10 == 0:
    print(remainder, end = "")
  else:
    print(remainder, end = ",")
  user = user//10   
#-------------------------------------------------------------------
#task11

user = int(input("Sir,Please enter your desired number: "))
tick = 0

while user>0:
  user = user//10
  tick += 1
print(tick)    
#-------------------------------------------------------------------
#task12 final

num1 = int(input())

num = num1

counter = 0

while num>0:
  num = num//10
  counter += 1

while counter > 0:

  if counter == 1:
    print(num1//10**(counter-1))
  else:
    print(num1//10**(counter-1),end = ",")

  num1 = num1%10**(counter-1)
  counter -= 1   
#-------------------------------------------------------------------
#task13

user = int(input("Sir,Please enter your desired number: "))
divisor = 1
counter = 0

while divisor<=user:
  if user%divisor == 0:
    counter = counter + 1
    print(divisor)
  divisor += 1
print("Total {} divisors.".format(counter))  
    
#-------------------------------------------------------------------
#task14

var = int(input("Sir,Please enter your desired number: "))
divisor = 1
sum = 0

while divisor<var:
  if var%divisor == 0:
    sum = sum+divisor
  divisor += 1

if sum == var:
  print("{} is a perfect number!".format(var))
else:
  print("{} is not a perfect number!".format(var))   
#-------------------------------------------------------------------
#task15

user = int(input("Sir,Please enter a number: "))
divisor = 0
counter = 1

while counter<=user:
     if user%counter == 0:
          divisor+=1
     counter+=1
if user%1==0 and user%user==0 and divisor==2:
    print("{} is a prime number".format(user))
else:
   print("{} is not a prime number".format(user))
#-------------------------------------------------------------------
#task16

no_of_inps = int(input("How many numbers you want to take: "))
min = 0
max = 0
sum = 0
for x in range(0, no_of_inps, 1):
  num=int(input())
  if x == 0:
    min = num
    max = num
    sum = num
  else:
    sum += num
    if num >= max:
      max = num
    if num <= min:
      min = num
print(f'Maximum {max}')
print(f'Minimum {min}')
print(f'Average is {sum/no_of_inps}')    
#-------------------------------------------------------------------
#task 17 

N = int(input("Sir,Please enter the size: "))

for row in range(N):
    for column in range(N):
        print("+",end="")
    print()   
#-------------------------------------------------------------------
#task 18 

M = int(input("enter the height: "))
N = int(input("enter the length: "))

for row in range(1,M+1):
    for column in range(1,N+1):
        print(column,end="")
    print()   
#-------------------------------------------------------------------
#task 19 

N = int(input("enter the height: "))
sum = 0

for row in range(1,N+1):
    for column in range(1,row+1):
        print(column,end="")
    print()    
#-------------------------------------------------------------------
#---------------------TRACING------------------20-24
#-------------------------------------------------------------------
#task25

N = int(input("enter a number: "))

fibo1 = 0 
fibo2 = 1 
new = 0 

for i in range(N+1):
    
    if i == 0: 
        print(fibo1,end = " ")

    elif i == 1 :
        print(fibo2,end = " ")

    else: 
        new = fibo1 + fibo2 

        if new <= N: 

            fibo1 = fibo2 
            fibo2 = new 
            
            print(new,end=" ")

        
#-------------------------------------------------------------------
#Task25's Program to display the Fibonacci sequence up to n-th term
#another format

nterms = int(input("How many terms? "))

# first two terms
n1, n2 = 0, 1
count = 0

# check if the number of terms is valid
if nterms <= 0:
   print("Please enter a positive integer")
# if there is only one term, return n1
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
# generate fibonacci sequence
else:
   print("Fibonacci sequence:")
   for i in range(nterms):
       print(n1)
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth

#-------------------------------------------------------------------
#task26

num = int(input("Sir,Please enter a number: "))

temp = num 
bin = 0 
digit = 0 
count = 0

while temp > 0: 

    digit = (temp % 2) * (10**count)
    bin += digit 
    temp //= 2 
    count += 1

print(bin)
#-------------------------------------------------------------------
# task 27

input = int(input("Sir,Please enter a number: "))
digit = len(str(input))

temp = input
new = 0
count = 0

while input > 0 : 

    temp = input % 10 
    new += temp * (2**count)
    count += 1 
    input //= 10 

print(new)
#-------------------------------------------------------------------
#task28

start = int(input("start: "))
end = int(input("end: "))

div = 0 
div_last = 0
sum = 0 
prime = 0 
prime_st = ""
perfect = 0 
perfect_st = ""

print(f'Between {start} and {end},')

for i in range(start,end+1):

    for q in range(1,i+1):

         
        if i % q == 0:
            sum += q
            div += 1 
            #if q == i:
               # div_last = i

    if div == 2: 
        prime += 1
        if i == div_last:        
            prime_st += str(i)
        else:
            prime_st += str(i) + ", "

    if sum - i == i:
        perfect += 1 
        if i == end:
            perfect_st += str(i)
        else:
            perfect_st += str(i) + ", "

    div = 0 
    sum = 0 
print(f'found {prime} prime numbers') 
print(f'found {perfect} perfect numbers') 
print(f'Prime numbers are {prime_st}')
print(f'Perfect numbers are {perfect_st}')
#-------------------------------------------------------------------
# task 29

n1 = int(input("start: "))
d1 = len(str(n1))


n2 = int(input("end: "))
d2 = len(str(n2))                              # when d1 = d2


n3 = int(input("divisor: "))


for i in range(n1,n2+1):        
    m = 1
    for j in range(d1):  
        x = str(i)
        x = x[j]                              
        m = m * int(x)
        continue
    
   
    if m % n3 == 0:
        print(m)