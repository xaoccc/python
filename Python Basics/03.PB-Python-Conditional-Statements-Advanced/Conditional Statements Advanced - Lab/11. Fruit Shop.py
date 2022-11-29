fruit = input().lower()
day = input().lower()
q = float(input())
price = 0

if  day == "saturday" or day == "sunday" :
    if fruit == "banana" :
        price = 2.70*q
    elif fruit == "apple" :
        price = 1.25*q
    elif fruit == "orange" :
        price = 0.90*q
    elif fruit == "grapefruit" :
        price = 1.60*q
    elif fruit == "kiwi" :
        price = 3.00*q
    elif fruit == "pineapple" :
        price = 5.60*q
    elif fruit == "grapes" :
        price = 4.20*q
elif day == "monday" or day == "tuesday" or day == "wednesday" or day == "thursday" or day == "friday" :
    if fruit == "banana" :
        price = 2.50*q
    elif fruit == "apple" :
        price = 1.20*q
    elif fruit == "orange" :
        price = 0.85*q
    elif fruit == "grapefruit" :
        price = 1.45*q
    elif fruit == "kiwi" :
        price = 2.70*q
    elif fruit == "pineapple" :
        price = 5.50*q
    elif fruit == "grapes" :
        price = 3.85*q
if price != 0 :
    print (f"{price:.2f}")
else :
    print ("error")