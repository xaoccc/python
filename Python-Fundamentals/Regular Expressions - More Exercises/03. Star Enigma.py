import re
planets_num = int(input())
decode_data = ["s", "t", "a", "r"]
attacked, destroyed, planets = [], [], []
pattern = r"@(?P<planet>[a-zA-Z]+)([^\@\-\!\:\>]*):(?P<population>[0-9]+)([^\@\-\!\:\>]*)(\!)(?P<attack>[A,D])!([^\@\-\!\:\>]*)->(?P<army>[0-9]+)"

for i in range(planets_num):
    count = 0
    planet_name = ""
    planet = input()
    for j in planet:
        if j.lower() in decode_data:
            count += 1
    for j in planet:
        planet_name += chr(ord(j) - count)
    planets.append(planet_name)

for p in planets:
    match = re.finditer(pattern, p)
    for i in match:
        if i["attack"] == "A":
            attacked.append(i["planet"])
        elif i["attack"] == "D":
            destroyed.append(i["planet"])
attacked = sorted(attacked)
destroyed = sorted(destroyed)
print(f"Attacked planets: {len(attacked)}")
for planet in attacked:
    print(f"-> {planet}")
print(f"Destroyed planets: {len(destroyed)}")
for planet in destroyed:
    print(f"-> {planet}") 
