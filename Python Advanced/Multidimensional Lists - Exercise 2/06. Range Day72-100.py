shoot_area = [input().split() for i in range(5)]
count_targets, total_targets, curr_pos, shot_targets = 0, 0, [], []
for i in range(5):
    if "A" in shoot_area[i]:
        curr_pos = [i, shoot_area[i].index("A")]
    if "x" in shoot_area[i]:
        total_targets += shoot_area[i].count("x")
def mark_visited(pos, steps):
    shoot_area[curr_pos[0]][curr_pos[1]] = "."
    curr_pos[pos] += steps
    shoot_area[curr_pos[0]][curr_pos[1]] = "A"
    
def move(direction, steps, curr_pos):
    if direction == "right":
        if curr_pos[1] + steps < 5 and shoot_area[curr_pos[0]][curr_pos[1] + steps] != "x":
            mark_visited(1, steps)
    elif direction == "left":
        if curr_pos[1] - steps >= 0 and shoot_area[curr_pos[0]][curr_pos[1] - steps] != "x":
            mark_visited(1, -steps)
    elif direction == "up":
        if curr_pos[0] - steps >= 0 and shoot_area[curr_pos[0] - steps][curr_pos[1]] != "x":
            mark_visited(0, -steps)
    elif direction == "down":
        if curr_pos[0] + steps < 5 and shoot_area[curr_pos[0] + steps][curr_pos[1]] != "x":
            mark_visited(0, steps)
    return 

def shoot(a, b, count_):
    global count_targets
    shot_targets.append([a, b])
    count_targets += 1
    shoot_area[a][b] = "."    

for i in range(int(input())):
    command = input().split()
    if command[0] == "move":
        move(command[1], int(command[2]), curr_pos)

    elif command[0] == "shoot":
        direction = command[1]
        if direction == "right":
            for i in range(curr_pos[1], 5):
                if shoot_area[curr_pos[0]][i] == "x":
                    shoot(curr_pos[0], i, count_targets)
                    break
                
        elif direction == "left":
            for i in range(curr_pos[1] - 1, -1, -1):
                if shoot_area[curr_pos[0]][i] == "x":
                    shoot(curr_pos[0], i, count_targets)
                    break
                    
        elif direction == "up":
            for i in range(curr_pos[0] - 1, -1, -1):
                if shoot_area[i][curr_pos[1]] == "x":
                    shoot(i, curr_pos[1], count_targets)
                    break
                    
        elif direction == "down":
            for i in range(curr_pos[0], 5):
                if shoot_area[i][curr_pos[1]] == "x":
                    shoot(i, curr_pos[1], count_targets)
                    break

    if count_targets == total_targets:
        print(f"Training completed! All {count_targets} targets hit.")
        break
else:       
    print(f"Training not completed! {total_targets - count_targets} targets left.")
    
for target in shot_targets:         
    print(target)
