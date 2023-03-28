import re
pattern = r"(?P<type>[A-Za-z]+)\((?P<data>.+)\)"
all_data = {}
taken = {}
db = []

command = input()
while command != "start_selling":
    match = re.match(pattern, command)
    current = match["data"].replace('"', "").split(", ")
    
    if (match["type"] == "OfficeApartment" or match["type"] == "LivingApartment") and len(current) < 5:
        print("__init__() missing 1 required positional argument: 'price'")
    elif match["type"] == "Apartment":
        print("Can't instantiate abstract class Apartment with abstract methods __str__")
        
    else:
        if match["type"] not in all_data:
            all_data[match["type"]] = {current[0]: current[1:]}
        else:
            all_data[match["type"]][current[0]] = current[1:]
        db.append(current[0])

    command = input()

action = input()
while action != "taken" and action != "free":
    action = action.split()
    if action[1] not in db:
        print(f"Apartment with id - {action[1]} does not exist!")
    elif action[0] == "rent" and action[1] not in all_data["OfficeApartment"].keys():
        print(f"Apartment with id - {action[1]} is only for selling!")
    elif action[0] == "buy" and action[1] not in all_data["LivingApartment"].keys():
        print(f"Apartment with id - {action[1]} is only for renting!")
    elif action[0] == "rent" and action[1] in all_data["OfficeApartment"].keys():
        if "OfficeApartment" not in taken.keys():
            taken["OfficeApartment"] = {action[1]: all_data["OfficeApartment"][action[1]]}
        else:
            taken["OfficeApartment"][action[1]] = all_data["OfficeApartment"][action[1]]
        del all_data["OfficeApartment"][action[1]]
    elif action[0] == "buy" and action[1] in all_data["LivingApartment"].keys():
        if "LivingApartment" not in taken.keys():
            taken["LivingApartment"] = {action[1]: all_data["LivingApartment"][action[1]]}
        else:
            taken["LivingApartment"][action[1]] = all_data["LivingApartment"][action[1]]
        del all_data["LivingApartment"][action[1]]
    action = input()
    
  
if (action == "taken" and len(taken) == 0) or (action == "free" and len(all_data) == 0):
    print("No information for this query")
elif action == "taken":
    taken = dict(sorted(taken.items(), key = lambda x: x[0], reverse=True))
    for i in taken:
        taken[i] = dict(sorted(taken[i].items(), key = lambda x: (x[1][3], -int(x[1][2]))))
    for key, value in taken.items():
        for ap, ap_data in value.items():
            print(f"{ap_data[0]} rooms place with {ap_data[1]} bathroom/s.")
            print(f"{float(ap_data[2])} sq. meters for {float(ap_data[3])} lv.")

elif command == "free":
    all_data = dict(sorted(all_data.items(), key = lambda x: x[0], reverse=True))
    for i in all_data:
        all_data[i] = dict(sorted(all_data[i].items(), key = lambda x: (x[1][3], -int(x[1][2]))))
    for key, value in all_data.items():
        for ap, ap_data in value.items():
            print(f"{ap_data[0]} rooms place with {ap_data[1]} bathroom/s.")
            print(f"{float(ap_data[2])} sq. meters for {float(ap_data[3])} lv.")
