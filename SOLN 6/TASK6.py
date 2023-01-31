#first_version

given_tuple = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h')
a_list = list(given_tuple)
a_list = a_list[::-1]
final_tuple = tuple(a_list)
print(final_tuple)

#second_version

t = given_tuple = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h')
a = list(t)
b = []

for i in range(len(a)-1,-1,-1):
    b.append(a[i])

ft = final_tuple = tuple(b)
print(ft)