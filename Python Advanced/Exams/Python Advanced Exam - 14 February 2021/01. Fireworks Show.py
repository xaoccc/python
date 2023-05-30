from collections import deque
firework_effects, explosive_power = deque([int(i) for i in input().split(", ")]), deque([int(i) for i in input().split(", ")])
fireworks = {
    "Palm Fireworks": 0,
    "Willow Fireworks": 0,
    "Crossette Fireworks": 0
}
show = False
epic_fail = False
while firework_effects and explosive_power:
    while firework_effects[0] <= 0 or explosive_power[-1] <= 0:
        if firework_effects[0] <= 0:
            firework_effects.popleft()
        if explosive_power[-1] <= 0:
            explosive_power.pop()
        if not firework_effects or not explosive_power:
            epic_fail = True
            break
    
    if epic_fail:
        break
    current_firework_effect = firework_effects.popleft()
    current_explosive_power = explosive_power.pop()
    
        
    firework = current_firework_effect + current_explosive_power
    if firework % 3 == 0 and firework % 5 != 0:
        fireworks["Palm Fireworks"] += 1
    elif firework % 3 != 0 and firework % 5 == 0:
        fireworks["Willow Fireworks"] += 1
    elif firework % 3 == 0 and firework % 5 == 0:
        fireworks["Crossette Fireworks"] += 1
    else:
        firework_effects.append(current_firework_effect - 1)
        explosive_power.append(current_explosive_power)
    
    if fireworks["Palm Fireworks"] >= 3 and fireworks["Willow Fireworks"] >= 3 and fireworks["Crossette Fireworks"] >= 3:
        show = True

if show:
    print("Congrats! You made the perfect firework show!")
if not show:
    print("Sorry. You can't make the perfect firework show.")

if firework_effects:
    print(f"Firework Effects left: {', '.join([str(i) for i in firework_effects])}")
if explosive_power:
    print(f"Explosive Power left: {', '.join([str(i) for i in explosive_power])}")

for key, value in fireworks.items():
    print(f"{key}: {value}")
