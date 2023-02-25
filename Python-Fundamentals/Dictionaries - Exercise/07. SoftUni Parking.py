vehicles_num = int(input())
parking_system = {}

for i in range(vehicles_num):
    command = input().split()
    username = command[1]
    if len(command) == 3:
        plate_number = command[2]
    if command[0] == "register":
        if username in parking_system:
            print(f"ERROR: already registered with plate number {plate_number}")
        else:
            parking_system[username] = plate_number
            print(f"{username} registered {plate_number} successfully")
    else:
        if username not in parking_system:
            print(f"ERROR: user {username} not found")
        else:
            del parking_system[username]
            print(f"{username} unregistered successfully")

    
for (key, value) in parking_system.items():
    print(f"{key} => {value}")
