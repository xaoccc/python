import re
plants_num = int(input())
plants = {}
pattern = r"[^\-\:]"
for i in range(plants_num):
    plant_info = [int(i) if i.isdigit() else i for i in input().split("<->")]
    plants[plant_info[0]] = [plant_info[1], [0]]

command = input()
while command != "Exhibition":
    command = "".join(re.findall(pattern, command)).split()
    if command[0] == "Rate":
        if command[1] in plants.keys():
            if plants[command[1]][1][0] == 0:
                plants[command[1]][1][0] = int(command[2])
            else:
                plants[command[1]][1].append(int(command[2]))
        else:
            print("error")
    elif command[0] == "Update":
        if command[1] in plants.keys():
            plants[command[1]][0] = int(command[2])
        else:
            print("error")
    elif command[0] == "Reset":
        if command[1] in plants.keys():
            plants[command[1]][1] = [0]
        else:
            print("error")
    command = input()
print("Plants for the exhibition")
for plant, plant_stats in plants.items():
    average_rating = sum(plant_stats[1]) / len(plant_stats[1])
    print(f"{plant}; Rarity: {plant_stats[0]}; Rating: {average_rating:.2f}")
