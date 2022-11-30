fruit = input()
pack = input()
num = int(input())
 
if pack == "small":
    num *= 2
    if fruit == "Watermelon":
        price = 56
    elif fruit == "Mango":
        price = 36.66
    elif fruit == "Pineapple":
        price = 42.1
    elif fruit == "Raspberry":
        price = 20
elif pack == "big":
    num *= 5
    if fruit == "Watermelon":
        price = 28.7
    elif fruit == "Mango":
        price = 19.6
    elif fruit == "Pineapple":
        price = 24.8
    elif fruit == "Raspberry":
        price = 15.2
total = price * num
if 400 <= total <= 1000:
    total *= 0.85
elif total > 1000:
    total *= 0.5
print(f"{total:.2f} lv.")
