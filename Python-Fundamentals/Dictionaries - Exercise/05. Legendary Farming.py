key_materials = {"shards": 0, "fragments": 0,  "motes": 0}
junk = {}

while True:
    if key_materials["shards"] >= 250:
        key_materials["shards"] -= 250
        print("Shadowmourne obtained!")
        break
    elif key_materials["fragments"] >= 250:
        key_materials["fragments"] -= 250
        print("Valanyr obtained!")
        break
    elif key_materials["motes"] >= 250: 
        key_materials["motes"] -= 250
        print("Dragonwrath obtained!")
        break

    materials = input().split()
    materials = [i.lower() for i in materials]
    
    for i in range(0, len(materials), 2):
        if materials[i+1] in key_materials:
            key_materials[materials[i+1]] += int(materials[i])
        if materials[i+1] not in key_materials:
            if materials[i+1] not in junk:
                junk[materials[i+1]] = 0
            junk[materials[i+1]] += int(materials[i])
            
        if key_materials["shards"] >= 250 or key_materials["fragments"] >= 250 or key_materials["motes"] >= 250:
            break

for (key, value) in key_materials.items():
    print(f"{key}: {value}")
for (key, value) in junk.items():
    print(f"{key}: {value}")
