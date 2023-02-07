items_list = input().split(", ")
command = input()

while command != "Craft!":
    command = command.split(" - ")
    if command[0] == "Collect":
        if command[1] not in items_list:
            items_list.append(command[1])
    elif command[0] == "Drop":
        if command[1] in items_list:
            items_list.remove(command[1])
    elif command[0] == "Combine Items":
        old_new = command[1].split(":")
        
        if old_new[0] in items_list:
            old_index = items_list.index(old_new[0])
            items_list.insert(old_index + 1, old_new[1])
    elif command[0] == "Renew":
        if command[1] in items_list:
            items_list.append(items_list.pop(items_list.index(command[1])))
    command = input()
print(", ".join(items_list))
