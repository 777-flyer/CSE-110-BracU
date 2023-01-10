#task1

a_list = []
for i in range (5):
  user = int(input("Sir,Please enter your desired number: "))
  a_list.append(user)
  print("Numbers in the list: {}".format(a_list))
  
  
#task2

#s = user = "10, 20, 24, 25, 26, 35, 70"
u = user = input()
ns = new_string = ""

for i in user:
  if i != " ":
    ns += i
  else:
    pass

a_list = []
bin = ""

for i in ns:
  if i != ",":
    bin += i
  else:
    a_list.append(int(bin))
    bin = ""


a_list.append(int(bin))
length = len(a_list)

if length > 3:
    print(a_list[2:length-2])
else:
    print("Not possible")
    



#task3
a_list = []
for i in range (5):
  user = int(input())
  a_list.append(user)
rev_list = a_list[::-1]

for j in rev_list:
  print(j)
  
  
#task4

given_list = [3, 5, 1, 6]
length = len(given_list)
new_list = n = []
for i in range (length):
    given_list[i] = (given_list[i]**2)
    new_list.append(given_list[i])
print(new_list)



#task5

given_list = ["hey", "there", "", "what's", "", "up", "", "?"]
length = len(given_list)
new_list = nl = []
for i in range(length):
  if given_list[i] == "":
    continue
  else:
    nl.append(given_list[i])
print("ORIGINAL LIST: {} ".format(given_list))
print("MODIFIED LIST: {} ".format(nl))


#task6

given_numbers = nums = "7, 13, 2, 10, 6, -11, 0"
length = len(nums)
substr = ""
for i in range(length):
  if nums[i] != " ":
      substr += nums[i]
  else:
      pass

a_list = []
ano_str = ""
for j in substr:
  if j != ",":
    ano_str += j
  else:
    a_list.append(int(ano_str))
    ano_str = "" 

a_list.append(int(ano_str))
length = len(a_list)

#for max num

maxnum = 0
maxind = 0

for k in range(length):
  if a_list[k] > maxnum:
      maxnum = a_list[k]
      maxind = k

print("My list: {}".format(a_list))
print("Largest number in the list is {} which was found at index {}.".format(maxnum,maxind))


#task07

list_one = [1, 3, 5, 7, 9, 10]
list_two = [2, 4, 6, 8]
new_list = []

for i in list_one[:(len(list_one)-1)]:
  new_list.append(i)
for j in list_two:
  new_list.append(j)

print(new_list)


#task08

list_one = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list_two = [10, 11, 12, -13, -14, -15, -16]

new_list = []

for i in list_one:
  if i%2 == 0:
    new_list.append(i)
for j in list_two:
  if j%2 == 0:
    new_list.append(j)

print(new_list)


#task09

user = input()

bin = ""
a_list = []

for i in user:
  if i != " ":
    bin += i
  else:
    a_list.append(int(bin))
    bin = ""

a_list.append(int(bin))

mod_list = []

for new in a_list:
  if new%2 != 0:
    mod_list.append(new)

print("Original list: {}".format(a_list))
print("Modified list: {}".format(mod_list))




#task10

s = user = input("input: ")
#s = user = "0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4"
new_string =''

for i in user:
    if i != " ":
      new_string += i
    else:
      pass
new_string = new_string + ","

a_list = []
store = ""

for j in new_string:
    if j != ",":
      store += j
    else:
      a_list.append(int(store))
      store = ""

#a_list.append(int(store))

final_list = []
for k in a_list:
  if k not in final_list:
    final_list.append(k)


print("Input list: {}".format(a_list))
print("Modified list: {}".format(final_list))


#task 11 

list_one = [1, 4, 3, 2, 6]
list_two = [5, 6, 9, 8, 7]

temp = False

for i in list_one:
    if i in list_two:
        temp = True
        break

print(temp)
print(type(temp))


#task16

x = int(input("Please enter the number of elements: "))
a_list = []

for i in range(x):
  user = int(input("Please enter the numbers: "))
  a_list.append(user)

max_n = 0
max_in = 0
secmax = 0
secmaxin = 0

for j in range (len(a_list)):
  if a_list[j] > max_n:

    max_n = a_list[j]
    max_in = j

for k in range (len(a_list)):
  if a_list [k] > secmax and a_list [k] != max_n:

    secmax = a_list[k]
    secmaxin = k

print(a_list)
print("The second largest number is {} and it's index is {}".format(secmax,secmaxin))



#task 16 updated

x = int(input("number of elements: "))

list_a = []
for i in range(x):
    y = int(input(f"enter element_{i+1}: "))
    list_a.append(y)

print(f"My list: {list_a}")
# [7, 13, 2, 10, 6, -11, 0]

max_f = 0    #largest number
f_indx = 0   #index largest
max_s = 0    #second largest
s_indx = 0   #index second...

for i in range(len(list_a)):
    if list_a[i] > max_f:
        
        max_f = list_a[i]
        f_indx = i 

for i in range(len(list_a)):
    if list_a[i] > max_s and list_a[i] != max_f:
        
        max_s = list_a[i]
        s_indx = i    
     
print(max_f)
print(f_indx)
print(max_s)
print(s_indx)

print(f"Second largest number in the list is {max_s} which was found at index {s_indx}.")



#task 17

x = int(input('number of elements: '))

list_a = []

for i in range(x):
    y = int(input(f'element_{i+1}: '))
    list_a.append(y)

print(f'My list: {list_a}')

max = 0
mx_indx = 0 
min = 0 
mn_indx = 0

for i in range(len(list_a)): 
    if list_a[i] > max:
        max = list_a[i]
        mx_indx = i

    if list_a[i] < min:
        min = list_a[i]
        mn_indx = i

print(f"Smallest number in the list is {min} which was found at index {mn_indx}\nLargest number in the list is {max} which was found at index {mx_indx}")



#task 18

list_1 = []
list_2 = []

x = int(input("number of elements in list_1: "))
for i in range(x):
    p = input(f"list_1 element_{i+1}: ")
    list_1.append(p)

y = int(input("number of elements in list_2: "))
for i in range(y):
    q = input(f"list_2 element_{i+1}: ")   
    list_2.append(q)

print(list_1)
print(list_2)

new_list = [] # list with common elements from list_1 & list_2

for i in list_2:
    if i in list_1:
        new_list.append(i)

print(new_list)



# task 19 

list_one = [1, 2, 2, 4, 5, 5, 7, 99, 200, 303, 70]
list_two = [1, 1, 2, 3, 3, 3, 4, 5, 200, 500, -5]

new_list = []

for i in list_one:
    if i not in new_list:
        new_list.append(i)

for i in list_two:
    if i not in new_list:
        new_list.append(i)

print(new_list)


#task 20 ***

s = user_input = "      [1,   2   ,         3,   50,   4]       "
print(f'Original data: {s}')


nsw = new_string_without_white_space = s.strip()

ns = ""

for i in nsw:
    if i != "[" and i != "]" :
        ns += i
       
print(f'After removing square brackets: {ns}') # 1,   2   ,         3,   50,   4

temp = ""
new_list = []

for i in ns:
    if i != ",":
        temp += i 
    else:
        new_list.append(temp)
        temp = ""

new_list.append(temp)

print(f'Numbers in string format with extra white spaces: {new_list}') # ['1', '   2   ', '         3', '   50', '   4']

temp = ""
final_string = fs = ""

for i in ns:
    if i != " ":
        temp += i 
    else:
        fs += temp
        temp = ""
fs += temp
print("fs",fs) # 1,2,3,50,4

final_list = []
temp = ""
for i in fs:
    if i != ",":
        temp += i   
    else:
        final_list.append(int(temp))
        temp = ""
final_list.append(int(temp))

print(f'Final data (numbers in list format): {final_list}')


#task 21

#s = input('enter a string: ')
s = "0, 0, 1, 2, 3, 4,      4, 5, 6, 6, 6,      7, 8, 9, 4,         4"

new_string = ns = ""
temp = ""

for i in s:
    if i != " ":
        temp += i
    else:
        ns += temp
        temp = ""
ns += temp
#print(ns)

temp = ""
new_list = []

for i in ns:
    if i != ",":
        temp += i 
    else: 
        new_list.append(int(temp))
        temp = ""
new_list.append(int(temp))

print(f'Given numbers in list: {new_list}')

final_list = []

for i in new_list:
    if i not in final_list:
        final_list.append(i)

print(f'List without any dupliacte values: {final_list}')