from collections import deque

green_light = int(input())
green_light_restore = green_light
free_window = int(input())
traffic_data = deque()
successfully_passed_cars = 0
crash = False
green = 0

command = input()
while command != "END":
    traffic_data.append(command)
    if command == "green":
        green += 1
    command = input()

while traffic_data:
    if traffic_data[0] != "green":
        car = traffic_data.popleft()
        if len(car) <= green_light:
            successfully_passed_cars += 1
            green_light -= len(car)
        elif len(car) <= (green_light + free_window) and green_light > 0:
            successfully_passed_cars += 1
            green_light = 0
        elif green_light + free_window == 0 and green > 0:
            successfully_passed_cars += 1
            green_light = green_light_restore
            del traffic_data[traffic_data.index("green")]
            green -= 1
        elif len(car) > (green_light + free_window) and green_light > 0:
            print(f"A crash happened!\n{car} was hit at {car[(green_light + free_window) - len(car)]}.")
            crash = True
            break

    else:
        green_light = green_light_restore
        traffic_data.popleft()
        green -= 1
if not crash:
    print(f"Everyone is safe.\n{successfully_passed_cars} total cars passed the crossroads.")