import re
text = input()
valid_data = []

data_test = re.findall(r'[#|][a-zA-Z ]+[|#]\d{2}\/\d{2}\/\d{2}[|#][0-9]+[#|]', text)

for i in data_test:
    current_data = []
    if i[0] == "#" and i[-1] == "#":
        
        current_data = i.split("#")
        if len(current_data) == 5:
            valid_data.append(current_data[1:4])
    elif i[0] == "|" and i[-1] == "|":
        current_data = i.split("|")
        if len(current_data) == 5:
            valid_data.append(current_data[1:4])

print(valid_data)
