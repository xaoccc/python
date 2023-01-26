dungeon_rooms = input().split("|")
health = 100
coins = 0

for room in range(1, len(dungeon_rooms) + 1):
    current_room = dungeon_rooms[room-1].split()
    if current_room[0] == "potion":
        initial_health = health
        if health < 100:
            health += int(current_room[1])
            if health > 100:
                health = 100
        print(f"You healed for {health - initial_health} hp.")
        print(f"Current health: {health} hp.")
    elif current_room[0] == "chest":
        coins += int(current_room[1])
        print(f"You found {int(current_room[1])} bitcoins.")
    else:
        health -= int(current_room[1])
        if health <= 0:
            health = 0
            print(f"You died! Killed by {current_room[0]}.")
            print(f"Best room: {room}")
            break
        else:
            print(f"You slayed {current_room[0]}.")
if health > 0:
    print(f"You've made it!\nBitcoins: {coins}\nHealth: {health}")
