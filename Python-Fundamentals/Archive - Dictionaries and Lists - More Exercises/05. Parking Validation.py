import re
commands_num = int(input())
database = {}

for i in range(commands_num):
    command = input().split()
    
    if command[0] == "register":
        
        if command[2] in database.values():
            print(f"ERROR: license plate {match[0]} is busy")
        elif command[1] in database.keys():
            print(f"ERROR: already registered with plate number {database[command[1]]}")
        elif len(re.findall(r"[A-Z]{2}[0-9]{4}[A-Z]{2}", command[2])) == 1 and command[2] not in database.values() and command[1] not in database.keys():
            print(f"{command[1]} registered {command[2]} successfully")
            database[command[1]] = command[2]
        else:
            print(f"ERROR: invalid license plate {command[2]}")
        
    elif command[0] == "unregister":
        if command[1] not in database.keys():
            print(f"ERROR: user {command[1]} not found")
        else:
            print(f"user {command[1]} unregistered successfully")
            del database[command[1]]
for user, plate in database.items():
    print(f"{user} => {plate}")
