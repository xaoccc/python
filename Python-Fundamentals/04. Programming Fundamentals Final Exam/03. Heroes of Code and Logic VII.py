heroes_num = int(input())
heroes = {}

for i in range(heroes_num):
    hero = input().split()
    heroes[hero[0]] = [int(hero[1]), int(hero[2])]

command = input()

while command != "End":
    command = command.split(" - ")
    if command[0] == "CastSpell":
        if command[1] in heroes.keys() and heroes[command[1]][1] >= int(command[2]):
            heroes[command[1]][1] -= int(command[2])
            print(f"{command[1]} has successfully cast {command[3]} and now has {int(heroes[command[1]][1])} MP!")
        else:
            print(f"{command[1]} does not have enough MP to cast {command[3]}!")
    elif command[0] == "TakeDamage":
        if command[1] in heroes.keys() and heroes[command[1]][0] > int(command[2]):
            heroes[command[1]][0] -= int(command[2])
            print(f"{command[1]} was hit for {command[2]} HP by {command[3]} and now has {heroes[command[1]][0]} HP left!")
        else:
            heroes[command[1]][0] = 0
            print(f"{command[1]} has been killed by {command[3]}!")
        
    elif command[0] == "Recharge":
        if command[1] in heroes.keys():
            if heroes[command[1]][1] + int(command[2]) <= 200:
                print(f"{command[1]} recharged for {command[2]} MP!")
                heroes[command[1]][1] += int(command[2])
            else:
                print(f"{command[1]} recharged for {200 - heroes[command[1]][1]} MP!")
                heroes[command[1]][1] = 200
            
    elif command[0] == "Heal":
        if command[1] in heroes.keys():
            if heroes[command[1]][0] + int(command[2]) <= 100:
                print(f"{command[1]} healed for {command[2]} HP!")
                heroes[command[1]][0] += int(command[2])
            else:
                print(f"{command[1]} healed for {100 - heroes[command[1]][0]} HP!")
                heroes[command[1]][0] = 100
    
    command = input()
for hero, hero_stats in heroes.items():
    if hero_stats[0] > 0:
        print(f"{hero}\n  HP: {hero_stats[0]}\n  MP: {hero_stats[1]}")
