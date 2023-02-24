products_list = {}

command = input()
while command != "buy":
    command = command.split()
    product_name = command[0]
    product_price = float(command[1])
    product_qty = int(command[2])
    if product_name not in products_list:
        products_list[product_name] = [product_price, product_qty]
    else:
        products_list[product_name][1] += product_qty
        if products_list[product_name][0] != product_price:
            products_list[product_name][0] = product_price
        
    command = input()
for (key, value) in products_list.items():
    print(f"{key} -> {value[0] * value[1]:.2f}")
