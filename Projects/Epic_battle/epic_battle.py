import random
dungeons_number = random.randint(5, 15)

health = 1000
coins = 0

print("You'll going to fight terrible monsters! Prepare yourself!")
dungeon_rooms = []
for i in range(dungeons_number):
    dungeons_contents = random.choice(["small_potion", "big_potion", "chest", "rat", "bat", "orc", "wild_dog", "demon", "dinosaur", "lawyer", "mad_woman", "archdemon", "angry_teenager", "harpy", "small_chest", "big_chest"])
    if dungeons_contents == "small_potion":
        qty = random.randint(20, 50)
    elif dungeons_contents == "big_potion":
        qty = random.randint(50, 100)
    elif dungeons_contents == "chest":
        qty = random.randint(50, 100)
    elif dungeons_contents == "rat" or dungeons_contents == "bat" or dungeons_contents == "wild_dog" or dungeons_contents == "harpy" or dungeons_contents == "angry_teenager":
        qty = random.randint(30, 60)
    elif dungeons_contents == "orc" or dungeons_contents == "demon" or dungeons_contents == "lawyer":
        qty = random.randint(70, 100)
    elif dungeons_contents == "dinosaur" or dungeons_contents == "archdemon" or dungeons_contents == "mad_woman":
        qty = random.randint(150, 250)
    elif dungeons_contents == "small_chest":
        qty = random.randint(50, 100)
    elif dungeons_contents == "big_chest":
        qty = random.randint(100, 200)
    
    dungeon_rooms.append(dungeons_contents + " " + str(qty))

for room in range(1, len(dungeon_rooms) + 1):

    current_room = dungeon_rooms[room-1].split()
    if current_room[0].find("potion") > -1:
        initial_health = health
        if health < 1000:
            health += int(current_room[1])
            if health > 1000:
                health = 1000
        print(f"You healed for {health - initial_health} hp.")
        print(f"Current health: {health} hp.")
    elif current_room[0].find("chest") > -1:
        coins += int(current_room[1])
        print(f"You found {int(current_room[1])} bitcoins.")
    else:
        weapon = input("Hero, choose your weapon:")
        health -= int(current_room[1])
        if health <= 0:
            health = 0
            print(f"You died! Killed by {current_room[0]}.")
            print(f"Best room: {room}")
            break
        else:
            print(f"You slayed {current_room[0]}({int(current_room[1])}HP) with {weapon}.")
            print(f"Health remaining: {health} hp.")
if health > 0:
    print(f"You've made it!\nBitcoins: {coins}\nHealth: {health}")
        
