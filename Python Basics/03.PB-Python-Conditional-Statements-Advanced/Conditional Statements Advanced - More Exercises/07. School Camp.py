#user input
season = input().lower()
gender = input().lower()
students_num = int(input())
nights_num = int(input())
sport = ""

#logic
if gender == "boys":
    if season == "winter" :
        sport = "Judo"
        price = nights_num * 9.60
    elif season == "spring" :
        price = nights_num * 7.20
        sport = "Tennis"
    elif season == "summer" :
        price = nights_num * 15
        sport = "Football"
if gender == "girls":
    if season == "winter" :
        price = nights_num * 9.60
        sport = "Gymnastics"
    elif season == "spring" :
        price = nights_num * 7.20
        sport = "Athletics"
    elif season == "summer" :
        price = nights_num * 15
        sport = "Volleyball"
elif gender == "mixed" :
    if season == "winter" :
        price = nights_num * 10
        sport = "Ski"
    elif season == "spring" :
        price = nights_num * 9.50
        sport = "Cycling"
    elif season == "summer" :
        price = nights_num * 20
        sport = "Swimming"
price = price * students_num
if students_num >= 50 :
    price = price * 0.5
elif 20 <= students_num < 50 :
    price = price * 0.85
elif 10 <= students_num < 20 :
    price = price * 0.95

#output
print(f"{sport} {price:.2f} lv.")