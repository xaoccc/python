command = 0
min_num = 100000
while command != "Stop" :
    command = input()
    if command == "Stop":
        break
    if int(command) < min_num :
        min_num = int(command)
print(f"{int(min_num)}")