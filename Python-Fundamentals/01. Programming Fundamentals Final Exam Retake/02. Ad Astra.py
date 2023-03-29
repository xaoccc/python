import re
text = input()
valid_data = []
total_calories = 0
data_test = re.finditer(r'([#|])(?P<food>[a-zA-Z ]+)\1(?P<date>\d{2}\/\d{2}\/\d{2})\1(?P<calories>\d+)\1', text)

for i in data_test:
    valid_data.append([i["food"], i["date"], i["calories"]])
    total_calories += int(i["calories"])
            
print(f"You have food to last you for: {total_calories // 2000} days!")
for food in valid_data:
    print(f"Item: {food[0]}, Best before: {food[1]}, Nutrition: {food[2]}")
