#TASK01

user = input()

reversed_ver = user[::-1]

print(reversed_ver)

#task2

a = input()
b = int(input())
f = ""
f += a[b::-1]
f += a[(len(f)):]

print(f)

#task3

num = input()
num1 = int(num)
for i in range (len(num)):
     if num1 > 0: 
    
           if num1 % 10 == 0 or num1 % 10 == 1 and i == len(num):
                 
                 print("Binary Number")
                 
                 break
           
           elif num1 % 10 == 0 or num1 % 10 == 1:
                   
                   num1 = num1 // 10
           
           elif num1 % 10 != 0 or num1 % 10 != 1:
                    
                    print('Not a Binary number')
                    
                    break
     else:
            print('Not a Binary number')
            
            break
        
#task3_different_appraoch

num = input()


bin = 0

for i in range (len(num)):
     
     test = num[i]
     
     if test == "0" or test == "1":
          
          continue
     else:
         
         bin=1

if bin == 0:
    
    print("binary")

else:
    
    print('Not binary')
    
    
#task4

word = input()
word1 = word[::-1]
end = word1[0:3]
end1 = word1[0:2]
len = len(word)

if end == 'tse':
    
   print(word)
   
elif end1 == 're':
    
   a = word.replace("er","est")
   print(a)
   
elif len < 4:
    print(word)

elif len > 3:
    print(word+"er")
    
    
#task5

a = input()
l = len(a)

for i in range(l):
    
     if i == 0:
        print(a[i])
        
     elif i == len(a):
        print(a)
        
     else:
        print(a[:i+1:])
        

#task6

a = input()

for i in range(len(a)):
    
     char = a[i]
     num = ord(char)
     
     print("{} : {}".format(char,num))
     
     
#task7


word = input()
new_word = ""
counter = 0
while counter < len(word):
    if chr(ord(word[counter])) == "z":
        
        new_word += "a"
  
    else:
        
        new_word += chr(((ord(word[counter]))+1))
    
    counter+=1
    
print(new_word)

#task8

a = input()
lower = ""
for i in range (len(a)):
    
     if i % 2 != 0:
         
         lower += a[i]

upper = ""

for i in range (len(lower)):
    
    c = ord(lower[i])-32
    upper += chr(c)
    
print(upper)


#task9


a = input()
b = 0
c = ''
for i in range (len(a)):
    
    if i == 0:
        
        b += ord(a[i])
        c += a[i]
        
    elif ord(a[i]) != b:
        
          c += (a[i])
          b = ord(a[i])
          
print(c)


#task 10

# ABCD, efgh ---> AeBfCgDh
# ABCDENDFGH, ijkl ---> AiBjCkDlENDFGH
# ijkl, ABCDENDFGH ---> iAjBkClDENDFGH

s = user_input = input()
d = length = len(s)
x = index = 0 
n = new_word = ""
w1 = first_word = 0
w2 = second_word = 0
d1 = length_of_smaller_part = 0
d2 = length_of_bigger_part = 0

for i in range(d):
    if s[i] == ",":
        x = i 

w1 = s[:x]
print(w1)

w2 = s[x+2:]
print(w2)

if len(w1) < len(w2):
    d1 = len(w1)
    d2 = len(w2)
elif len(w1) > len(w2):
    d1 = len(w2)
    d2 = len(w1)

for j in range(d1):
    n = n + w1[j] + w2[j]

if len(w1) < len(w2):
    n = n + w2[d1:]
elif len(w1) > len(w2):
    n = n + w1[d2:]

print(n)



#-------------------------------------------


#task16

word = input()
letter = input()
f = ""
flag1 = 0

for char in word:
    
    if char == letter:
        
        flag1 = 1
        
        break
    
    else:
        
        continue

if flag1 == 1:
    
    for i in range (len(word)):
         
        if ord(word[i]) != ord(letter):
            
          f += word[i]
          
    print(f)

elif len(word) > 3:
    
     print(word[1:len(word)-1])

else:
    
     print(word)




#task17

word = input()
split = input()

f = ''
for i in range (len(word)):
    
    if ord(word[i]) == ord(split):
        
        f += "\n"
    
    else:
        
        f += word[i]
        
print(f)



#task18

string = input()

num = int(input())

if num % 2 == 0:
   
   print(string*(num*2))

else:
    
    print(string*(num*3))
    
    
    
    
#task19


word = input()
f = ''
flag = 0

for i in range (len(word)):
    
    if ord("A") > ord(word[i])   or   ord(word[i]) > ord("z"):
          
          f += word[i]
          
    elif i == 0:
        
        f += (word[i]).upper()
        
        flag = 1
        
    elif flag == 1:
        
        f += (word[i]).lower()
        
        flag=0
        
    elif flag == 0:
        f += (word[i]).upper()
        
        flag=1
        
        
print(f)


# task 19 ***

s = word = input()
n = new_word = ''
f = flag = 0

for i in range (len(s)):
    
    if ord(s[i]) < ord("A") or ord(s[i]) > ord("z") or 91 <= ord(s[i]) <= 96:
        
        n += s[i]

    elif i == 0:
        
        n += s[i].upper()
        
        f = 1
    
    elif f == 1:
        
        n += s[i].lower()
        
        f = 0
    
    elif f == 0:
        
        n += s[i].upper()   
        
        f = 1

print(n)