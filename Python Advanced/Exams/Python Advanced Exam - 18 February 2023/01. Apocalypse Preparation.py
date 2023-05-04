from collections import deque

textiles = deque([int(i) for i in input().split()])
medicaments = deque([int(i) for i in input().split()])
first_aid_kit = {"Patch": [30, 0], "Bandage": [40, 0], "MedKit": [100, 0]}

while textiles and medicaments:
    textile = textiles.popleft()
    medicament = medicaments.pop()
    healing_item = False
    for key, value in first_aid_kit.items():
        if value[0] == textile + medicament:
            first_aid_kit[key][1] += 1
            healing_item = True
            break
    if not healing_item:
        if textile + medicament > first_aid_kit["MedKit"][0]:
            first_aid_kit["MedKit"][1] += 1
            medicaments[-1] += (textile + medicament - first_aid_kit["MedKit"][0])
        else:
            medicaments.append(medicament + 10)
    if len(textiles) == 0 and len(medicaments) == 0:
        print("Textiles and medicaments are both empty.")
        break
    elif len(textiles) == 0:
        print("Textiles are empty.")
        break
    elif len(medicaments) == 0:
        print("Medicaments are empty.")
        break
first_aid_kit = dict(sorted(first_aid_kit.items(), key=lambda x: (-x[1][1], x[0])))


for key, value in first_aid_kit.items():
    if value[1] > 0:
        print(f"{key} - {value[1]}")

medicaments = sorted(list(medicaments), reverse=True) 
if len(medicaments) > 0:
    print(f"Medicaments left: {', '.join([str(i) for i in medicaments])}")
if len(textiles) > 0:
    print(f"Textiles left: {', '.join([str(i) for i in textiles])}")
