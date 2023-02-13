pirate_status = [int(i) for i in input().split(">")]
warship_status = [int(i) for i in input().split(">")]
max_hp = int(input())
command = input()
lost = False

while command != "Retire":
    damaged = 0
    command = command.split()
    if command[0] == "Fire":
        if 0 <= int(command[1]) < len(pirate_status):
            warship_status[int(command[1])] -= int(command[2])
            if warship_status[int(command[1])] < 0:
                print("You won! The enemy ship has sunken.")
                lost = True
                break
        
    elif command[0] == "Defend":
        if 0 <= int(command[1]) < len(pirate_status) and 0 <= int(command[2]) < len(pirate_status):
            for i in range(int(command[1]), int(command[2]) + 1):
                pirate_status[i] -= int(command[3])
                if pirate_status[i] < 0:
                    print("You lost! The pirate ship has sunken.")
                    lost = True
                    break
    
    elif command[0] == "Repair":
        if 0 <= int(command[1]) < len(pirate_status):
            pirate_status[int(command[1])] += int(command[2])
            if pirate_status[int(command[1])] > max_hp:
                pirate_status[int(command[1])] = max_hp
        
    elif command[0] == "Status":
        for i in pirate_status:
            if i < max_hp * 0.2:
                damaged += 1 
        print(f"{damaged} sections need repair.")
    if lost == False:
        command = input()
    else: 
        break

if lost == False:
    print(f"Pirate ship status: {sum(pirate_status)}\nWarship status: {sum(warship_status)}")
