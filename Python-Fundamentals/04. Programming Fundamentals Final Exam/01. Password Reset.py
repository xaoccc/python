password = input()
command = input()
while command != "Done":
    command = command.split()
    if command[0] == "TakeOdd":
        password = password[1::2]
        print(password)
    elif command[0] == "Cut":
        password = password[ :int(command[1])] + password[int(command[1])+int(command[2]): ]
        print(password)
    elif command[0] == "Substitute":
        if password.find(command[1]) != -1:
            password = password.replace(command[1], command[2])
            print(password)
        else:
            print("Nothing to replace!")
    command = input()

print(f"Your password is: {password}")
