def individual_bonus_calculation (player_name,yearly_income,goal_scored,bonus):
    updated = 0
    if goal_scored > 30:
        
        updated = goal_scored * (bonus/100 * yearly_income) + 10000
    
    elif 20 <= goal_scored <= 30:
        
        updated = goal_scored * (bonus/100 * yearly_income) + 5000
    
    else:
        
        updated = goal_scored * (bonus/100 * yearly_income)
        
    updated = int(updated)
    return ("{} earned a bonus of {} Taka for {} goals.".format(player_name,updated,goal_scored))    
    
individual_bonus_calculation("Neymar", 1200000, 35, 5)





def cal_bonus(name, salary, goal, percentage,*extra):

    print(individual_bonus_calculation(name,salary,goal,percentage))
    
    for i in range(0,len(extra),4):
            print(individual_bonus_calculation(extra[i],extra[i+1],extra[i+2],extra[i+3]))
        
        
       

cal_bonus("Neymar",1200000, 35, 5,'Jamal', 700000, 19, 8,'Luis', 80000, 25, 10)
