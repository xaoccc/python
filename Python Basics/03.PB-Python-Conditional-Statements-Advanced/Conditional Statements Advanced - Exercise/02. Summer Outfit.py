degrees = int(input())
time_of_day = input().lower()
outfit = ""
shoes = ""

if  time_of_day == "morning" :
    if 10 <= degrees <= 18 : 
        outfit = "Sweatshirt"
        shoes = "Sneakers"
    elif 18 < degrees <= 24 : 
        outfit = "Shirt"
        shoes = "Moccasins"
    elif 24 < degrees : 
        outfit = "T-Shirt"
        shoes = "Sandals"
elif  time_of_day == "afternoon" :
    if 10 <= degrees <= 18 : 
        outfit = "Shirt"
        shoes = "Moccasins"
    elif 18 < degrees <= 24 : 
        outfit = "T-Shirt"
        shoes = "Sandals"
    elif 24 < degrees : 
        outfit = "Swim Suit"
        shoes = "Barefoot"
elif  time_of_day == "evening" :
        outfit = "Shirt"
        shoes = "Moccasins"
print (f"It's {degrees} degrees, get your {outfit} and {shoes}.")