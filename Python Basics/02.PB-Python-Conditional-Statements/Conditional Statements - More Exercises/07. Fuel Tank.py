#user input
fuel_type = input().lower()
fuel_available = int(input())

#logic and output
if fuel_type == "diesel" or  fuel_type == "gasoline" or fuel_type == "gas":
    if fuel_available >= 25 :
        print(f"You have enough {fuel_type}.")
    else :
        print(f"Fill your tank with {fuel_type}!")
else :
    print("Invalid fuel!")