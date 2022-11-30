food_available = int(input()) * 1000
food_eaten = input()
food_left = 0
total_food_eaten = 0
 
while food_eaten != "Adopted":
    total_food_eaten += int(food_eaten)
    food_eaten = input()
    if food_eaten == "Adopted":
        break
 
food_left = food_available - total_food_eaten
if food_available < total_food_eaten:
    print(f"Food is not enough. You need {abs(food_left)} grams more.")
else:
    print(f"Food is enough! Leftovers: {abs(food_left)} grams.")
