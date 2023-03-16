message = input()
command = input()
while command != "Reveal":
    command = [int(i) if i.isdigit() else i for i in command.split(":|:")]
    if command[0] == "InsertSpace":
        message = message[ :command[1]] + " " + message[command[1]: ]
    elif command[0] == "Reverse":
        if command[1] in message:
            message = message.replace(command[1], "", 1) + command[1][::-1]
        else:
            print("error")
            command = input()
            continue
    elif command[0] == "ChangeAll":
        message = message.replace(command[1], command[2])
    print(message)
    command = input()
print(f"You have a new text message: {message}")
