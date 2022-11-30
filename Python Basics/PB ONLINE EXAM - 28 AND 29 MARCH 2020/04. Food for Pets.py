days = int(input())
food_available = float(input())
food_day = 0
dog_food_total = 0
cat_food_total = 0
biscuits = 0
biscuits_total = 0 
    
for i in range (1, days+1):
    dog_food = int(input())
    cat_food = int(input())
    dog_food_total += dog_food
    cat_food_total += cat_food
    food_day = dog_food + cat_food
    if i % 3 == 0:
        biscuits = food_day * 0.1
        biscuits_total += biscuits
food_total = dog_food_total + cat_food_total

print(f"Total eaten biscuits: {round(biscuits_total)}gr.")
print(f"{(food_total * 100 / food_available):.2f}% of the food has been eaten.")
print(f"{(dog_food_total * 100 / food_total):.2f}% eaten from the dog.")
print(f"{(cat_food_total * 100 / food_total):.2f}% eaten from the cat.")
