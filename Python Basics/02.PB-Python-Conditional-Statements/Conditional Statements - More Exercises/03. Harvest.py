#user input
vineyard_area = int(input())
vineyard_prod = float(input())
wine_needed = int(input())
workers = int(input())
from math import ceil
from math import floor

#logic
wine_prod = (vineyard_area * 0.4 * vineyard_prod) / 2.5
if wine_prod <  wine_needed :
    print(f"It will be a tough winter! More {floor(wine_needed - wine_prod)} liters wine needed.")
else :
    wine_left = wine_prod - wine_needed
    print (f"Good harvest this year! Total wine: {ceil(wine_prod)} liters.")
    print(f"{ceil(wine_left)} liters left -> {ceil(wine_left / workers)} liters per person.")