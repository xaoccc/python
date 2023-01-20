wagons_num = int(input())
wagons_num_list = []
for i in range(wagons_num):
    wagons_num_list.append(0)
command = input()
while command != "End":
    command = command.split()
    if command[0] == "add":
        wagons_num_list[-1] += int(command[1])
    elif command[0] == "insert":
        wagons_num_list[int(command[1])] += int(command[2])
    elif command[0] == "leave":
        wagons_num_list[int(command[1])] -= int(command[2])
    command = input()
print(wagons_num_list)
