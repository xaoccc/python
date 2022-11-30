from math import ceil
people_num = int(input())
entry_price = float(input())
sunbed_price = float(input())
umb_price = float(input())
 
umbrellas = ceil(people_num / 2)
sunbeds = ceil(people_num * 0.75) 
total = (people_num * entry_price) + (umb_price * umbrellas) + (sunbeds * sunbed_price)
 
print(f"{total:.2f} lv." )
