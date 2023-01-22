gifts_list = input().split()
command = input()

while True:
    current_command = command.split()
    if current_command[0] == "OutOfStock":
        for i in range(len(gifts_list)):
            if gifts_list[i] == current_command[1]:
                gifts_list[i] = "None"

    if current_command[0] == "Required":
        if int(current_command[2]) < len(gifts_list):
            gifts_list[int(current_command[2])] = current_command[1]

    if current_command[0] == "JustInCase":
        gifts_list[-1] = current_command[1]

    command = input()
    if command == "No Money":
        for j in gifts_list:
            if j == "None":
                gifts_list.remove(j)
        break

print(" ".join(gifts_list))
