days = int(input()) - 1
accomodation = input()
rating = input()

if rating == "positive" :
    if accomodation == "room for one person" :
        price = 18*days
    elif accomodation == "apartment" :
        if days < 10 :
            price = 25*days*0.7
        elif days <= 15 :
            price = 25*days*0.65
        elif days > 15 :
            price = 25*days*0.50
    elif accomodation == "president apartment" :
        if days < 10 :
            price = 35*days*0.9
        elif days <= 15 :
            price = 35*days*0.85
        elif days > 15 :
            price = 35*days*0.80
    price *= 1.25
elif rating == "negative" :
    if accomodation == "room for one person" :
        price = 18*days
    elif accomodation == "apartment" :
        if days < 10 :
            price = 25*days*0.7
        elif days <= 15 :
            price = 25*days*0.65
        elif days > 15 :
            price = 25*days*0.50
    elif accomodation == "president apartment" :
        if days < 10 :
            price = 35*days*0.9
        elif days <= 15 :
            price = 35*days*0.85
        elif days > 15 :
            price = 35*days*0.80
    price *= 0.90
print(f"{price:.2f}")
    
