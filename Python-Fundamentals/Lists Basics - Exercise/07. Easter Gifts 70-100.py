gifts_list = input().split()
command = input()

while command != "No Money":
    command = command.split()
    if command[0] == "OutOfStock":
        for i in range(len(gifts_list)):
            if gifts_list[i] == command[1]:
                gifts_list[i] = "None"

    elif command[0] == "Required":
        if 0 <= int(command[2]) < len(gifts_list):
            gifts_list[int(command[2])] = command[1]
    elif command[0] == "JustInCase":
        gifts_list[-1] = command[1]
    command = input()
    
for j in gifts_list:
    if "None" in gifts_list:
        gifts_list.remove("None")

print(*gifts_list)
