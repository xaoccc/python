gifts_list = input()
gifts_list = gifts_list.split(" ")
command = input()
while True:
    command = command.split(" ")
    if "OutOfStock" in command:
        for i in range(len(gifts_list)):
            if gifts_list[i] == command[1]:
                gifts_list[i] = "None"
    if "Required" in command:
        if int(command[2]) < len(gifts_list) and int(command[2]) > -1:
            gifts_list[int(command[2])] = command[1]
    if "JustInCase" in command:
        gifts_list[-1] = command[1]
    command = input()
    if command == "No Money":
        for j in gifts_list:
            if j == "None":
                gifts_list.remove(j)
        break
    

print(" ".join(gifts_list))
