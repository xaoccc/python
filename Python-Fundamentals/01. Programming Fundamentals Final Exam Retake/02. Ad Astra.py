text = "#Bread#19/03/21#4000#|Invalid|03/03.20||Apples|08/10/20|200||Carrots|06/08/20|500||Not right|6.8.20|5|"
valid_data = []
if text[0] == "#" or text[0] == "|":
    text = text[1: ]
if text[-1] == "#" or text[-1] == "|":
    text = text[:-1 ]

    
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
            valid_data.append(i) 
        print(i)
    else:
        i = i.split("|")
        if len(i) == 3:
            valid_data.append(i) 
print(valid_data)
