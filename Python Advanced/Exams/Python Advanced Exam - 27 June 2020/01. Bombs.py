from collections import deque

bomb_effect, bomb_casting = deque([int(i) for i in input().split(", ")]), deque([int(i) for i in input().split(", ")])
bombs = {
    "Datura Bombs": [40, 0],
    "Cherry Bombs": [60, 0],
    "Smoke Decoy Bombs": [120, 0]
}


while bomb_effect and bomb_casting:
    bomb_crafting = False
    success = False
    current_bomb_effect = bomb_effect.popleft()
    current_bomb_casting = bomb_casting.pop()
    for key, value in bombs.items():
        if current_bomb_effect + current_bomb_casting == value[0]:
            bomb_crafting = True
            bombs[key][1] += 1

    if bombs["Datura Bombs"][1] >= 3 and bombs["Cherry Bombs"][1] >= 3 and bombs["Smoke Decoy Bombs"][1] >= 3:
        success = True
        print("Bene! You have successfully filled the bomb pouch!")
        break

    if not bomb_crafting:
        bomb_effect.appendleft(current_bomb_effect)
        bomb_casting.append(current_bomb_casting - 5)


if not success:
    print("You don't have enough materials to fill the bomb pouch.")

if not bomb_effect:
    print("Bomb Effects: empty")
else:
    print(f"Bomb Effects: {', '.join(str(i) for i in bomb_effect)}")

if not bomb_casting:
    print("Bomb Casings: empty")
else:
    print(f"Bomb Casings: {', '.join(str(i) for i in bomb_casting)}")

print(f"Cherry Bombs: {bombs['Cherry Bombs'][1]}\nDatura Bombs: {bombs['Datura Bombs'][1]}\nSmoke Decoy Bombs: {bombs['Smoke Decoy Bombs'][1]}")

