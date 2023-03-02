usernames = input().split(", ")
result = []
for i in usernames:
    newstring = ""
    if 2 < len(i) < 17:
        for j in i:
            if not j.isdigit() and not j.isalpha() and j != "-" and j != "_":
                newstring = ""
                break
            else:
                newstring += j
        result.append(newstring)
        
for i in result:
    if len(i) > 2:
        print(i)
