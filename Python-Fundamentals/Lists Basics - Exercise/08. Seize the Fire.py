cells_fire = input().split("#")
water = int(input())
fire = 0
fire_type = ""
fire_lvl = 0
effort = 0
print("Cells:")

for cell in cells_fire:
    cell = cell.split()
    fire_lvl = int(cell[2])
    fire_type = cell[0]
    
    if (fire_type == "Low" and (1 <= fire_lvl <= 50)) \
    or (fire_type == "Medium" and (51 <= fire_lvl <= 80)) \
    or (fire_type == "High" and (81 <= fire_lvl <= 125)) and water >= fire_lvl:
        water -= fire_lvl
        if water < 0:
            break
        fire += fire_lvl
        effort += fire_lvl * 0.25
        print(" - " + str(fire_lvl))
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {fire}")
