key_materials = {"shards": 0, "fragments": 0,  "motes": 0}
junk = {}

while True:
    materials = input().split()
    
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
