heroes_num = int(input())
heroes = {}

for i in range(heroes_num):
    hero = input().split()
    heroes[hero[0]] = [hero[1], hero[2]]

command = input()

while command != "End":
    command = command.split(" - ")
    if command[0] == "CastSpell":
        if command[1] in heroes.keys() and int(heroes[command[1]][1]) >= int(command[2]):
            heroes[command[1]][1] = int(heroes[command[1]][1])
            heroes[command[1]][1] -= int(command[2])
            print(f"{command[1]} has successfully cast {command[3]} and now has {int(heroes[command[1]][1])} MP!")
        else:
            print(f"{command[1]} does not have enough MP to cast {command[3]}!")
    elif command[0] == "TakeDamage":
        pass
    elif command[0] == "Reachrge":
        pass
    elif command[0] == "Heal":
        pass
    
    
    command = input()
