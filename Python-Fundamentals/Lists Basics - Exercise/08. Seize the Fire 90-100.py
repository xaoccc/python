cells_fire = input()
water = int(input())
cells_fire = cells_fire.split("#")
fire = 0
effort = 0
print("Cells:")
for i in range(len(cells_fire)):
    cells_fire[i] = cells_fire[i].split(" ")
    
    cells_fire[i][-1] = int(cells_fire[i][-1])
    if (cells_fire[i][0] == "Low" and (0 < cells_fire[i][-1] < 51)) or (cells_fire[i][0] == "Medium" and (50 < cells_fire[i][-1] < 81)) or (cells_fire[i][0] == "High" and (80 < cells_fire[i][-1] < 126)):
        water -= cells_fire[i][-1]
        if water < 0:
            break
        fire += cells_fire[i][-1]
        effort += cells_fire[i][-1] * 0.25
        print("- " + str(cells_fire[i][-1]))
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {fire}")
