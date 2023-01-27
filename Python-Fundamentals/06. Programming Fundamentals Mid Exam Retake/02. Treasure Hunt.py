treasure = input().split("|")
command = input()
stolen = []
treasure_gain = 0

while command != "Yohoho!":
    command = command.split()
    if command[0] == "Loot":
        for i in range(1, len(command)):
            if command[i] not in treasure:
                treasure.insert(0, command[i])
    
    elif command[0] == "Drop":
        if 0 <= int(command[1]) < len(treasure):
            treasure.append(treasure[int(command[1])])
            treasure.remove(treasure[int(command[1])])
    
    elif command[0] == "Steal":
        stolen = treasure[-int(command[1]):]
        if len(treasure) <= int(command[1]):            
            treasure = []
        else:
            del treasure[(len(treasure) - int(command[1])): ]

        print(", ".join(stolen))
    command = input()
    
if len(treasure) == 0:
    print("Failed treasure hunt.")
else:
    for i in range(len(treasure)):
        treasure_gain += len(treasure[i])
    treasure_gain /= len(treasure)
    print(f"Average treasure gain: {treasure_gain:.2f} pirate credits.")
