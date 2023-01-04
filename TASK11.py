#"Python programming is fun"
user = "Python programming is fun"
user = user.lower()
print(user)
ns = ""
for i in user:
    if i != " ":
        ns += i

new_dict = {}
key = ""
value = 0

for k in range (len(ns)):
    for v in range (len(ns)):
        if ns[k] == ns[v]:
            key = ns[k]
            value += 1
            new_dict.update({f'{key}':value})
    value = 0
    
print(new_dict)       