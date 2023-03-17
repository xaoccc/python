cars_num = int(input())
cars = {}
for car in range(cars_num):
    car_data = [int(i) if i.isdigit() else i for i in input().split("|")]
    cars[car_data[0]] = [car_data[1], car_data[2]]
command = input()
while command != "Stop":
    command = command.split(" : ")
    if command[0] == "Drive":
        if command[1] in cars.keys():
            if int(command[3]) > cars[command[1]][1]:
                print("Not enough fuel to make that ride")
            else:
                cars[command[1]][1] -= int(command[3])
                cars[command[1]][0] += int(command[2])
                print(f"{command[1]} driven for {command[2]} kilometers. {command[3]} liters of fuel consumed.")
                if cars[command[1]][0] >= 100000:
                    print(f"Time to sell the {command[1]}!")
                    del cars[command[1]]
        
    elif command[0] == "Refuel":
        if command[1] in cars.keys():
            if cars[command[1]][1] + int(command[2]) > 75:
                print(f"{command[1]} refueled with {75 - cars[command[1]][1]} liters")
                cars[command[1]][1] = 75
            else: 
                cars[command[1]][1] += int(command[2])
                print(f"{command[1]} refueled with {int(command[2])} liters")
                
    elif command[0] == "Revert":
        if command[1] in cars.keys():
            if cars[command[1]][0] - int(command[2]) >= 10000:
                cars[command[1]][0] -= int(command[2])
                print(f"{command[1]} mileage decreased by {int(command[2])} kilometers")
            else:
                cars[command[1]][0] = 10000
    command = input()
for car_name, car_stats in cars.items():
    print(f"{car_name} -> Mileage: {car_stats[0]} kms, Fuel in the tank: {car_stats[1]} lt.")
