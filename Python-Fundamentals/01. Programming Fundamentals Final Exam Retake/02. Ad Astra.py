import re
text = input()
valid_data = []

if text[0] == "#" or text[0] == "|":
    text = text[1: ]
if text[-1] == "#" or text[-1] == "|":
    text = text[ :-1]

    
if "||" in text:
    text = text.replace("||", "divide!!!")
if "#|" in text:
    text = text.replace("#|", "divide!!!")
if "|#" in text:
    text = text.replace("|#", "divide!!!")
text = text.split("divide!!!")    

for i in text:
    print(i)
    if "#" in i:
        i = i.split("#")
        if len(i) == 3:
            date_test = re.match(r'^\d{2}\/\d{2}\/\d{2}$', i[1])
            if date_test:
                valid_data.append(i) 
        print(i)
    else:
        i = i.split("|")
        if len(i) == 3:
            date_test = re.match(r'^\d{2}\/\d{2}\/\d{2}$', i[1])
            if date_test:
                valid_data.append(i) 
print(valid_data)
