from collections import deque
materials, magic = deque([int(i) for i in input().split()]), deque([int(i) for i in input().split()])
gifts = {
    "Diamond Jewellery": [400, 0],
    "Gemstone": [100, 0],
    "Gold": [300, 0],
    "Porcelain Sculpture": [200, 0],
}
while materials and magic:
    current_material = materials.pop()
    current_magic = magic.popleft()
    mm_sum = current_material + current_magic
    if mm_sum < 100:
        if mm_sum % 2 == 0:
            current_material *= 2
            current_magic *= 3
            mm_sum = current_material + current_magic
        else:
            mm_sum *= 2
            
    if mm_sum > 499:
        mm_sum /= 2
            
    if 100 <= mm_sum <= 499:
        for item in gifts.keys():
            if 0 <= mm_sum - gifts[item][0] < 100:
                gifts[item][1] += 1
                break
    
if (gifts["Gemstone"][1] >= 1 and gifts["Porcelain Sculpture"][1] >= 1) or (gifts["Gold"][1] >= 1 and gifts["Diamond Jewellery"][1] >= 1):
    print("The wedding presents are made!")
else:
    print("Aladdin does not have enough wedding presents.")
    
if materials:
    print(f"Materials left: {', '.join([str(i) for i in materials])}")
if magic:
    print(f"Magic left: {', '.join([str(i) for i in magic])}")
   
for key, value in gifts.items():
    if value[1] > 0:
        print(f"{key}: {value[1]}")
