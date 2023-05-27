import os

command = input()
while command != "End":
    command = command.split("-")
    if command[0] == "Create":
        with open(command[1], "w") as new_file:
            new_file.write("")
    elif command[0] == "Add":
        with open(command[1], "a") as new_file:
            new_file.write(command[2]+"\n")

    elif command[0] == "Replace":
        try:
            with open(command[1], "r") as new_file:
                text = new_file.read().replace(command[2], command[3])
            with open(command[1], "w") as new_file:
                new_file.write(text)
        except FileNotFoundError:
            print("File not found!")

    elif command[0] == "Delete":
        try:
            os.remove(command[1])
        except FileNotFoundError:
            print("File not found!")
    command = input()