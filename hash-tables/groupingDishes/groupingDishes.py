def groupingDishes(dishes: list):
    result = {}
    for ingredient, *names in dishes:
        for dish in names:
            result.setdefault(dish, []).append(ingredient)
    
    return [[name] + sorted(result[name])
            for name in sorted(result)
            if len(result[name]) > 1]

dishes = [["Cheese","Quesadilla","Sandwich"], 
        ["Salad","Salad","Sandwich"], 
        ["Sauce","Pizza","Quesadilla","Salad"], 
        ["Tomato","Pizza","Salad","Sandwich"]]
groupingDishes(dishes)
