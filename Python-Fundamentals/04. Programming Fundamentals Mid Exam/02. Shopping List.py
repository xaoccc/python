shopping_list = input().split("!")
command = input()

while command != "Go Shopping!":
    command = command.split()
    if command[0] == "Urgent":
        if shopping_list.count(command[1]) == 0:
            shopping_list.insert(0, command[1])
    elif command[0] == "Unnecessary":
        if shopping_list.count(command[1]) > 0:
            shopping_list.remove(command[1])
    elif command[0] == "Correct":
        if shopping_list.count(command[1]) > 0:
            for i in range(len(shopping_list)):
                if shopping_list[i] == command[1]:
                    shopping_list[i] = command[2]
    elif command[0] == "Rearrange": 
        if shopping_list.count(command[1]) > 0:
            shopping_list.remove(command[1])
            shopping_list.append(command[1])
            
    command = input()
print(", ".join(shopping_list))
