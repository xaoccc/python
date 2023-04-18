from collections import deque

green_light = int(input())
green_light_restore = green_light
free_window = int(input())
traffic_data = deque()
successfully_passed_cars = 0
crash = False

command = input()
while command != "END":
    traffic_data.append(command)
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
        elif len(car) > (green_light + free_window) and green_light > 0:
            print(f"A crash happened!\n{car} was hit at {car[(green_light + free_window) - len(car)]}.")
            crash = True
            break
    else:
        green_light = green_light_restore
        traffic_data.popleft()
if not crash:
    print(f"Everyone is safe.\n{successfully_passed_cars} total cars passed the crossroads.")
