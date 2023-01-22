total_price = 0
total_price_notax = 0


while True:
    command_input = input()
    if command_input == "special":
        total_price = total_price_notax * 1.2 * 0.9
        break
    elif command_input == "regular":
        total_price = total_price_notax * 1.2
        break
    elif float(command_input) < 0:
        print("Invalid price!")
    else:
        total_price_notax += (float(command_input))
if total_price == 0:
    print("Invalid order!")
else:
    print(f"Congratulations you've just bought a new computer!\nPrice without taxes: {total_price_notax:.2f}$\nTaxes: {total_price_notax / 5:.2f}$ \n-----------\nTotal price: {total_price:.2f}$")
