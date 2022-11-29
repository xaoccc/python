#user input
budget = float(input())
season = input().lower()
car_class = ""
car_type = ""

#logic
if budget <= 100 :
    car_class = "Economy class"
    if season == "summer" :
        car_type = "Cabrio"
        budget = budget * 0.35
    elif season == "winter" :
        car_type = "Jeep"
        budget = budget * 0.65
elif 100 < budget <= 500 :
    car_class = "Compact class"
    if season == "summer" :
        car_type = "Cabrio"
        budget = budget * 0.45
    elif season == "winter" :
        car_type = "Jeep"
        budget = budget * 0.80
elif budget > 500 :
    car_class = "Luxury class"
    car_type = "Jeep"
    budget = budget * 0.90
    
#output
print(f"{car_class}")
print(f"{car_type} - {budget:.2f}")