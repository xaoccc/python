total_steps = 0
steps = 0
goal = 10000
while total_steps < goal:
    steps = input()
    if steps == "Going home":
        steps_to_home = int(input())
        total_steps += steps_to_home
        if total_steps < goal:
            print(f"{goal - total_steps} more steps to reach goal.")
            break
    else:
        total_steps += int(steps)
    
if total_steps >= goal:
    print("Goal reached! Good job!")
    print(f"{total_steps - goal} steps over the goal!")