from collections import deque
materials = deque(map(int, input().split()))
magic = deque(map(int, input().split()))
crafted_presents = []
needed_presents_one = set(["Doll", "Wooden train"])
needed_presents_two = set(["Teddy bear", "Bicycle"])
presents = {"Doll": 150, "Wooden train": 250, "Teddy bear": 300, "Bicycle": 400}

while materials and magic:
    current_material = materials.pop()
    current_magic = magic.popleft()
    if current_material * current_magic in presents.values():
        for key, value in presents.items():
            if value == current_material * current_magic:
                crafted_presents.append(key)
                break
        
    elif current_magic * current_material < 0:
        materials.append(current_magic + current_material)
    
    elif current_material > 0 and current_magic > 0:
            materials.append(current_material + 15)
    else:
        if current_material > 0:
            materials.append(current_material)
        if current_magic > 0:
            magic.appendleft(current_magic)

if set(crafted_presents) >= needed_presents_one or set(crafted_presents) >= needed_presents_two:
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials:
    print(f"Materials left: {', '.join(map(str, reversed(materials)))}")
if magic:
    print(f"Magic left: {', '.join(map(str, magic))}")
for i in range(len(set(crafted_presents))):
    print(f"{list(sorted(set(crafted_presents)))[i]}: {crafted_presents.count(list(sorted(set(crafted_presents)))[i])}")
