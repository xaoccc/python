green_light = int(input())
green_light_restore = green_light
free_window = int(input())
traffic_data = []
successfully_passed_cars = 0
crash = False

command = input()
while command != "END":
    traffic_data.append(command)
    command = input()

for car in traffic_data:
    if car != "green":
        if len(car) < green_light:
            successfully_passed_cars += 1
            green_light -= len(car)
        elif (green_light + free_window) >= len(car) >= green_light:
            if green_light > 0:
                successfully_passed_cars += 1
                green_light = 0
        elif len(car) > (green_light + free_window) and green_light == 0:
            traffic_data.append(car)
        elif len(car) > (green_light + free_window) and green_light > 0:
            print(f"A crash happened!\n{car} was hit at {car[(green_light + free_window) - len(car)]}.")
            crash = True
            break
    else:
        green_light = green_light_restore

if not crash:
    print(f"Everyone is safe.\n{successfully_passed_cars} total cars passed the crossroads.")
