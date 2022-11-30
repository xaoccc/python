groups = int(input())
musala = 0
mnb = 0
kilim = 0
k2 = 0
everest = 0
total = 0
    
for group in range (0, groups):
    group_num = int(input())
    total += group_num
    if group_num <= 5:
        musala += group_num
    elif group_num <= 12:
        mnb += group_num
    elif group_num <= 25:
        kilim += group_num
    elif group_num <= 40:
        k2 += group_num
    else:
        everest += group_num
print(f"{musala * 100 / total:.2f}%")
print(f"{mnb * 100 / total:.2f}%")
print(f"{kilim * 100 / total:.2f}%")
print(f"{k2 * 100 / total:.2f}%")
print(f"{everest * 100 / total:.2f}%")
