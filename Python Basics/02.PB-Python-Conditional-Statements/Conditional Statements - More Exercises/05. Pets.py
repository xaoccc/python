#user input
days = int(input())
food = float(input())
dog_food = float(input())
cat_food = float(input())
turtle_food = float(input())
from math import ceil
from math import floor

#logic and output
enough_food = (dog_food * days) + (cat_food * days) + ((turtle_food * days) / 1000)
if food < enough_food :
    print(f"{ceil(enough_food - food)} more kilos of food are needed.")
else :
    print(f"{floor(food - enough_food)} kilos of food left.")