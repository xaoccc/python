def shop_from_grocery_list(budget, groceries_list, *products):
    bought_products = []
    
    for product in products:
        if product[0] in groceries_list and product[0] not in bought_products:
            if product[1] <= budget:
                budget -= product[1]
                groceries_list.remove(product[0])
                bought_products.append(product[0])
            else:
                break
        if not groceries_list:
            return f"Shopping is successful. Remaining budget: {budget:.2f}."
        
    return f"You did not buy all the products. Missing products: {', '.join(groceries_list)}."
