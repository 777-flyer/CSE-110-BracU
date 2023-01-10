item_number = int(input("Sir,Please enter the number of items you want to buy: "))


item_list = []


for num in range (0,item_number):
    item = input("Sir,Please enter the item name: ")
    item_list.append(item)
    
print("THE LIST: {}".format(item_list))

item_dict = {"Rice":105,"Potato":20,"Chicken":250,"Beef":510,"Oil":85}

def grocery_items (item_list, location = "Dhanmondi"):
    
    total = 0
    length = len(item_list)
    
    for count in range (0, length):
        
        total += item_dict[item_list[count]]
        
        
    if location == "Dhanmondi":
        total += 30
    else:
        total += 70
        
    return total
    
print(grocery_items(item_list, "Banani"))
