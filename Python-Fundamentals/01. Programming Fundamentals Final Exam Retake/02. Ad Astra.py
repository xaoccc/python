import re
text = input()
valid_data = []
total_calories = 0
data_test = re.findall(r'[#|][a-zA-Z ]+[|#]\d{2}\/\d{2}\/\d{2}[|#][0-9]+[#|]', text)

for i in data_test:
    current_data = []
    if i[0] == "#" and i[-1] == "#":
        current_data = i.split("#")
        if len(current_data) == 5:
            valid_data.append(current_data[1:4])
            total_calories += int(current_data[3])
    elif i[0] == "|" and i[-1] == "|":
        current_data = i.split("|")
        if len(current_data) == 5:
            valid_data.append(current_data[1:4])
            total_calories += int(current_data[3])
            
print(f"You have food to last you for: {total_calories // 2000} days!")
for item in valid_data:
    print(f"Item: {item[0]}, Best before: {item[1]}, Nutrition: {item[2]}")
