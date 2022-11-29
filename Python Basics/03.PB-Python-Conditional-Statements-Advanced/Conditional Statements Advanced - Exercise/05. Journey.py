budget = float(input())
season = input()
destination = ""
accomodation = ""

if season == "summer" :
    if budget <= 100 :
        price = budget * 0.3
        destination = "Bulgaria"
        accomodation = "Camp"
    elif budget <= 1000 :
        price = budget * 0.4
        destination = "Balkans"
        accomodation = "Camp"
    elif budget > 1000 :
        price = budget * 0.9
        destination = "Europe"
        accomodation = "Hotel"
elif season == "winter" :
    accomodation = "Hotel"
    if budget <= 100 :
        price = budget * 0.7
        destination = "Bulgaria"
    elif budget <= 1000 :
        price = budget * 0.8
        destination = "Balkans"
    elif budget > 1000 :
        price = budget * 0.9
        destination = "Europe"

print (f"Somewhere in {destination}")
print (f"{accomodation} - {price:.2f}")