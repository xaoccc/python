stops = input()
command = input().split(":")
while command[0] != "Travel":    
    if command[0] == "Add Stop":
        if 0 <= int(command[1]) < len(stops):
            stops = stops[ :int(command[1])] + command[2] + stops[int(command[1]): ]
    elif command[0] == "Remove Stop":
        if 0 <= int(command[1]) < len(stops) and 0 <= int(command[1]) < len(stops):
            stops = stops[ :int(command[1])] + stops[int(command[2]) + 1: ]
    elif command[0] == "Switch":
        stops = stops.replace(command[1], command[2])
    print(stops)
    command = input().split(":")
print(f"Ready for world tour! Planned stops: {stops}")
