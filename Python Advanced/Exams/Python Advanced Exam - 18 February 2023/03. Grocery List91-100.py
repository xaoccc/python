def shop_from_grocery_list(*args):
    budget = args[0]
    grocery_list = args[1]
    result = []
    product = 2
    while product < len(args) and budget >= 0:
        
        if budget >= 0 and grocery_list:
            budget -= args[product][1]
            if args[product][0] in grocery_list and budget >= 0:
                grocery_list.remove(args[product][0])
                
        product += 1 
        if not grocery_list and budget >= 0:
            return f"Shopping is successful. Remaining budget: {budget:.2f}."

    if budget < 0 or grocery_list:
        for i in range(len(grocery_list)):
            result.append(grocery_list[i])
        return f"You did not buy all the products. Missing products: {', '.join(result)}."
