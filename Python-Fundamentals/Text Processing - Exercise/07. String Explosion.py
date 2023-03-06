string = input()
result = ""
explosion_strength = 0
for i in range(len(string)):
    if string[i] != ">" and not string[i].isdigit():
        if explosion_strength == 0:
            result += string[i]
        else:
            explosion_strength -= 1
        
    if string[i].isdigit():
        explosion_strength += int(string[i])
        if explosion_strength == 0:
            result += "0"
        else:
            explosion_strength -= 1
        
    if string[i] == ">":
        result += ">"
        
print(result)
