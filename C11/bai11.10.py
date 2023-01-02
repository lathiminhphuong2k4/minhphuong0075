def menu_is_boring(meals):
    b= True
    for x in meals:
        if meals.count(x)!=1:
            b=False
            break
    return b
meals_1=['Cơm','Cá','Tôm','Thịt','Canh']
meals_2=['Cơm','Cơm','Cá','Tôm','Thịt']
print(menu_is_boring(meals_1))
print(menu_is_boring(meals_2))