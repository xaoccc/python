capacity = float(input())
total_luggage = 0
luggage_count = 0
 
while capacity >= total_luggage:
    luggage = input()
    if luggage == "End":
        print("Congratulations! All suitcases are loaded!")
        break
    luggage = float(luggage)
    luggage_count += 1
    if luggage_count % 3 == 0:
        luggage *= 1.1
    total_luggage += luggage
    if capacity < total_luggage:
        luggage_count -= 1
else:
    print("No more space!")
print(f"Statistic: {luggage_count} suitcases loaded.")
