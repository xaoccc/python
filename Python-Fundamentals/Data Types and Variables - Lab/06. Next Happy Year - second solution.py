year = int(input())
i = 0
while i < len(str(year)):
    if str(year).count(str(year)[i]) > 1:
        year += 1
        i = 0
    i += 1  
print(year)
