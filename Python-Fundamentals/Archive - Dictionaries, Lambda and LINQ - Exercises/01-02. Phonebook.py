phonebook = {}
command = input()
while command != "END":
    command = command.split()
    if command[0] == "A" and len(command) == 3:
        phonebook[command[1]] = command[2]
    elif command[0] == "S":
        if command[1] in phonebook.keys():
            print(f"{command[1]} -> {phonebook[command[1]]}")
        else:
            print(f"Contact {command[1]} does not exist.")
    elif command[0] == "ListAll":
        phonebook = dict(sorted(phonebook.items(), key=lambda x: x[0]))
        for person, phone_num in phonebook.items():
            print(f"{person} -> {phone_num}")
    command = input()
