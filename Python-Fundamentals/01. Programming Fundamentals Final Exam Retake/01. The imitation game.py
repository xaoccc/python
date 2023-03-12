message = input()
command = input()
decoded = ""

while command != "Decode":
    command = command.split("|")
    if command[0] == "Move":
        n = int(command[1])
        message = message[n: ] + message[ :n]
    elif command[0] == "Insert":
        value = command[2]
        index = int(command[1])
        message = message[:index] + value + message[index:]
    elif command[0] == "ChangeAll":
        message = message.replace(command[1], command[2])

    command = input()
print(f"The decrypted message is: {message}")