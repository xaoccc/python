def stock_availability(products, *commands):
    add_products, remove_products = False, False

    for command in commands:
        if command == "delivery":
            add_products = True
            remove_products = False
        elif command == "sell":
            add_products = False
            remove_products = True
            if commands.index(command) == len(commands) - 1:
                del products[0]
        else:
            if add_products:
                products.append(command)
            if remove_products:
                if type(command) is int:
                    if command < len(products):
                        products = products[command: ]
                    else:
                        products = []
                else:
                    if command in products:
                        products = [i for i in products if i != command]
                
    return products
