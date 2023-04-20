from collections import deque
materials = deque(map(int, input().split()))
magic = deque(map(int, input().split()))
crafted_presents = []
needed_presents_one = set(["Doll", "Wooden train"])
needed_presents_two = set(["Teddy bear", "Bicycle"])
presents = {"Doll": 150, "Wooden train": 250, "Teddy bear": 300, "Bicycle": 400}

while materials and magic:
    if materials[-1] * magic[0] in presents.values():
        for key, value in presents.items():
            if value == materials[-1] * magic[0]:
                crafted_presents.append(key)
                break
        materials.pop()
        magic.popleft()
    elif materials[-1] * magic[0] < 0:
        materials.append(materials.pop() + magic.popleft())
    elif materials[-1] == 0:
        materials.pop()
    elif magic[0] == 0:
        magic.popleft()
    else:
        magic.popleft()
        materials[-1] += 15
        
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
