given = 'I love Programming. Python is love.'
given_2 = ['@', '$', '&', '#']

ns = ""
ns_list = []
for i in given:
    if i != " " and i != ".":
        ns += i
    else:
        if ns != "":        
            ns_list.append(ns)
        ns = ""
        
dict = {}
sum = 0
length = len(given_2)
for k in ns_list:
    for v in k:
        sum += ord(v)
    key = given_2[sum%length]
    sum = 0
    if key not in dict:
        dict[key] = [k]
    elif k in dict[key]:
        pass
    else:
        dict[key].append(k)
print(dict)
        