def make_square (user):
    starting = user[0]
    ending  = user[1]
    new_dict = {}
    for i in range (starting,ending + 1):
        key = i
        value = i*i
        new_dict[key] = value
    return new_dict
print(make_square((5,9)))