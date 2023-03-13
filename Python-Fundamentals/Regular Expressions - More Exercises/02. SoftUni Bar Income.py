import re
sale_info = input()
total = 0

while sale_info != "end of shift":

    client_name = re.findall(r'(?<=\%)[A-Z][a-z]+(?=\%)', sale_info)
    product = re.findall(r'(?<=\<)\w+(?=\>)', sale_info)
    qty = re.search(r'(?<=\|)\d+(?=\|)', sale_info)
    price = re.search(r'(([0]|[1-9][0-9]*)\.[0-9]+\$)|([0]\$|[1-9][0-9]*\$)', sale_info)
    if len(client_name) == 1 and len(product) == 1 and qty and price:
        print(f"{client_name[0]}: {product[0]} - {int(qty.group()) * float(price.group()[:-1]):.2f}")
        total += int(qty.group()) * float(price.group()[:-1])

    sale_info = input()
print(f"Total income: {total:.2f}")
