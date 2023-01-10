#Jon:100, Dan:200, Rob:300
user = "Jon:100, Dan:200, Rob:300"
ns = ""

for i in user:
    if i != " ":
        ns += i
#Jon:100,Dan:200,Rob:300

ns = ns.replace(":",",")
s = ns.split(",")

list_1 = []
list_2 = []

for sp in range(len(s)):
    if sp % 2 == 0:
        list_1.append(s[sp])
    else:
        list_2.append(s[sp])
        
new_dict = {}

for k in range(len(list_1)):
    new_dict[list_1[k]] = int(list_2[k])
    
sum = 0
ctr = 0
for val in new_dict.values():
    sum += val
    ctr += 1
average = sum//ctr
print("The average is : {}".format(average))