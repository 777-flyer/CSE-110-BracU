g_inp = [(2, 3), (4, 5), (6, 7), (2, 8)]
k = 0
v = 0
vk = 0
a_list = []
for i in g_inp:
    k = i[0]
    v = i[1]
    vk = k*v
    a_list.append(vk)
    vk = 0
print(a_list)
