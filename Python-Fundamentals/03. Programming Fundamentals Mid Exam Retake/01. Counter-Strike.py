energy  = int(input())
command = input()
win = 0
while command != "End of battle":
    distance = int(command)
    if energy >= distance:
        energy -= distance
        if energy < 0:
            break
        win += 1
        if win % 3 == 0:
            energy += win
    else:
        break
    command = input()

if command == "End of battle":
    print(f"Won battles: {win}. Energy left: {energy}")
else:
    print(f"Not enough energy! Game ends with {win} won battles and {energy} energy")
