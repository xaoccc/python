def shopping_cart(*args):
    
    products = {
        "Soup": [],
        "Pizza": [],
        "Dessert": []
    }
    result = ""
    empty = False
    
    for item in args:
        if item == "Stop":
            if len(products["Soup"]) == 0 and len(products["Pizza"]) == 0 and len(products["Dessert"]) == 0:
                result = "No products in the cart!"
                empty = True
            break
        else:
            if item[0] == "Soup" and len(products["Soup"]) < 3 and item[1] not in products["Soup"]:
                products["Soup"].append(item[1])
            elif item[0] == "Pizza" and len(products["Pizza"]) < 4 and item[1] not in products["Pizza"]:
                products["Pizza"].append(item[1])
            elif item[0] == "Dessert" and len(products["Dessert"]) < 2 and item[1] not in products["Dessert"]:
                products["Dessert"].append(item[1])
    if not empty:
        products = dict(sorted(products.items(), key=lambda x: (-len(x[1]), x[0])))
        for key, value in products.items():
            result += f"{key}:\n"
            if value:
                for i in range(len(value)):
                    value[i] = " - " + value[i]
                value = '\n'.join(sorted(value))
                result += f"{value}\n"
    return result
