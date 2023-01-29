events = input().split("|")
energy = 100
coins = 100
fail = False
for i in range(len(events)):
    events[i] = events[i].split("-")
    action = events[i][0]
    points = int(events[i][1])
    if action == "rest":
        if (energy + points) <= 100:
            energy += points
            print(f"You gained {points} energy.")
            print(f"Current energy: {energy}.")
        else:
            print(f"You gained {points - (energy + points - 100)} energy.")
            print(f"Current energy: 100.")
            energy = 100
    elif action == "order":
        if energy >= 30:
            energy -= 30
            coins += points
            print(f"You earned {points} coins.")
        else:
            energy += 50
            print("You had to rest!")
    else:
        if coins >= points:
            coins -= points
            print(f"You bought {action}.")
        else:
            print(f"Closed! Cannot afford {action}." )
            fail = True
            break
if not fail:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")       
