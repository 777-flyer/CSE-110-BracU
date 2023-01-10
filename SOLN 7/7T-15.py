def grocery_shop (order_items,location = "Dhanmondi"):
    
    chart_given = {"Rice":105,"Potato":20,"Chicken":250,"Beef":510,"Oil":85}
    user_input = order_items
    price = 0
    
    for items in user_input:
        price += chart_given[items]
    if location == "Dhanmondi":
        price += 30
    else:
        price += 70
        
    return price

location = input("Sir,Please enter your location: ")
print(grocery_shop(order_items,location))