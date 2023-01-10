def individual_bonus_calculation (player_name,yearly_income,goal_scored,bonus):
    updated = 0
    if goal_scored > 30:
        
        updated = goal_scored * (bonus/100 * yearly_income) + 10000
    
    elif 20 >= goal_scored <= 30:
        
        updated = goal_scored * (bonus/100 * yearly_income) + 5000
    
    else:
        
        updated = goal_scored * (bonus/100 * yearly_income)
        
    updated = int(updated)
    print("{} earned a bonus of {} Taka for {} goals.".format(player_name,updated,goal_scored))    
    
individual_bonus_calculation("Neymar", 1200000, 35, 5)