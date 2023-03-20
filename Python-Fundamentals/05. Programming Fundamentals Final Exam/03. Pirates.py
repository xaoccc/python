sail_command = input()
cities = {}

while sail_command != "Sail":
    sail_command = sail_command.split("||")
    if sail_command[0] not in cities.keys():
        cities[sail_command[0]] = [int(sail_command[1]), int(sail_command[2])]
    else:
        cities[sail_command[0]][0] += int(sail_command[1])
        cities[sail_command[0]][1] += int(sail_command[2])
    sail_command = input()

command = input()
while command != "End":
    command = command.split("=>")
    if command[1] in cities.keys():
        if command[0] == "Plunder":
            cities[command[1]][0] -= int(command[2])
            cities[command[1]][1] -= int(command[3])
            print(f"{command[1]} plundered! {command[3]} gold stolen, {command[2]} citizens killed.")
            if cities[command[1]][0] == 0 or cities[command[1]][1] == 0:
                del cities[command[1]]
                print(f"{command[1]} has been wiped off the map!")

        elif command[0] == "Prosper":
            if int(command[2]) >= 0:
                cities[command[1]][1] += int(command[2])
                print(f"{int(command[2])} gold added to the city treasury. {command[1]} now has {cities[command[1]][1]} gold.")
            else:
                print("Gold added cannot be a negative number!")

    command = input()
if len(cities) == 0:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")
else:
    print(f"Ahoy, Captain! There are {len(cities)} wealthy settlements to go to:")
    for city, city_stats in cities.items():
        print(f"{city} -> Population: {city_stats[0]} citizens, Gold: {city_stats[1]} kg")