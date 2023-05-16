def shop_from_grocery_list(budget, grocery_list, *args):
    i = 0
    while i < len(args) and budget >= 0:
        product, price = args[i][0], args[i][1]
        
        if grocery_list:
            budget -= price
            if product in grocery_list and budget >= 0:
                grocery_list.remove(product)

        i += 1 
        if not grocery_list:
            return f"Shopping is successful. Remaining budget: {budget:.2f}."
           
    if budget < 0 or grocery_list:
        return f"You did not buy all the products. Missing products: {', '.join(grocery_list)}."
