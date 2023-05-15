def shop_from_grocery_list(budget, grocery_list, *args):
    product = 0
    while product < len(args) and budget >= 0:
        
        if budget >= 0 and grocery_list:
            budget -= args[product][1]
            if args[product][0] in grocery_list and budget >= 0:
                grocery_list.remove(args[product][0])

        product += 1 
        if not grocery_list:
            return f"Shopping is successful. Remaining budget: {budget:.2f}."
           
    if budget < 0 or grocery_list:
        return f"You did not buy all the products. Missing products: {', '.join(grocery_list)}."
