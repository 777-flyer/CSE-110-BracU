giv_dict = {'sci fi': 12, 'mystery': 15, 'horror': 8, 'mythology': 10, 'young_adult': 4, 'adventure':14}
max = 0
name = ""
for keys,values in giv_dict.items():
    if giv_dict[keys] > max:
        max = values
        name = keys
print("The highest selling book genre is '{}' and the max number is {}.".format(name,max))