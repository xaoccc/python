import re
command = input()
total_price = 0
print("Bought furniture:")
while command != "Purchase":
    pattern = r'>>[a-zA-Z]+<<[0-9]+(\.[0-9]+)?![0-9]+'
    furniture_input = re.match(pattern, command)
    if furniture_input:
        furniture = furniture_input.group().split("<<")
        furniture_info = furniture[1].split("!")
        furniture_price = float(furniture_info[0])
        furniture_qty = int(furniture_info[1])
        furniture = furniture[0].lstrip(">>")
        total_price += (furniture_price * furniture_qty)
        print(furniture)

    command = input()
print(f"Total money spend: {total_price:.2f}")
