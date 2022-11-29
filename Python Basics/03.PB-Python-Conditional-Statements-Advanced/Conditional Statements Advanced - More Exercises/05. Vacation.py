#user input
budget = float(input())
season = input().lower()
accomod = ""
car_type = ""

#logic
if budget <= 1000 :
    accomod = "Camp"
    if season == "summer" :
        budget = budget * 0.65
    elif season == "winter" :
        budget = budget * 0.45
elif 1000 < budget <= 3000 :
    accomod = "Hut"
    if season == "summer" :
        budget = budget * 0.80
    elif season == "winter" :
        budget = budget * 0.60
elif budget > 3000 :
    accomod = "Hotel"
    budget = budget * 0.90
    
if season == "summer" :
    location = "Alaska"
elif season == "winter" :
    location = "Morocco"

#output
print(f"{location} - {accomod} - {budget:.2f}")