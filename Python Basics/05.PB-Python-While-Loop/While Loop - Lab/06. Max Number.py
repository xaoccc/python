command = 0
max_num = -100000
while command != "Stop" :
    command = input()
    if command == "Stop":
        break
    if int(command) > max_num :
        max_num = int(command)
print(f"{int(max_num)}")