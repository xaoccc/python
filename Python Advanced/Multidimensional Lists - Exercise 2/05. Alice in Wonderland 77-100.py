map_size = int(input())
wonder_map = []
alice_alive = True
tea_collected = False
tea = 0

for row in range(map_size):
    wonder_map.append([int(i) if i.isdigit() or "-" in i else i for i in input().split()])
    if "A" in wonder_map[row]:
        alice_position = [row, wonder_map[row].index("A")]
current_position = alice_position


while True:
    wonder_map[current_position[0]][current_position[1]] = "*"
    direction = input()
    if not direction:
        break
    elif direction == "up":
        if current_position[0] >= 1:
            current_position[0] -= 1
            if wonder_map[current_position[0]][current_position[1]] == "R":
                alice_alive = False
            elif type(wonder_map[current_position[0]][current_position[1]]) is int:
                tea += wonder_map[current_position[0]][current_position[1]]
            if tea >= 10:
                tea_collected = True
        else:
            alice_alive = False
            
    elif direction == "down":
        if current_position[0] < map_size - 1:
            current_position[0] += 1
            if wonder_map[current_position[0]][current_position[1]] == "R":
                alice_alive = False
            elif type(wonder_map[current_position[0]][current_position[1]]) is int:
                tea += wonder_map[current_position[0]][current_position[1]]
            if tea >= 10:
                tea_collected = True
        else:
            alice_alive = False
            
    elif direction == "left":
        if current_position[1] >= 1:
            current_position[1] -= 1
            if wonder_map[current_position[0]][current_position[1]] == "R":
                alice_alive = False
            elif type(wonder_map[current_position[0]][current_position[1]]) is int:
                tea += wonder_map[current_position[0]][current_position[1]]
            if tea >= 10:
                tea_collected = True
        else:
            alice_alive = False
            
    elif direction == "right":
        if current_position[1] < map_size - 1:
            current_position[1] += 1
            if wonder_map[current_position[0]][current_position[1]] == "R":
                alice_alive = False
            elif type(wonder_map[current_position[0]][current_position[1]]) is int:
                tea += wonder_map[current_position[0]][current_position[1]]
            if tea >= 10:
                tea_collected = True
        else:
            alice_alive = False
    
    if tea_collected:
        wonder_map[current_position[0]][current_position[1]] = "*"
        print("She did it! She went to the party.")
        break
    
    if wonder_map[current_position[0]][current_position[1]] == "R":
        wonder_map[current_position[0]][current_position[1]] = "*"
        alice_alive = False
        
    if not alice_alive:
        print("Alice didn't make it to the tea party.")
        break
for i in wonder_map:
    print(*i)
