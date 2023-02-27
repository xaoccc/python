command = input()
all_data = {}

while command != "no more time":
    command = command.split(" -> ")
    username = command[0]
    contest = command[1]
    points = int(command[2])
    if username not in all_data:
        all_data[username] = {}
        all_data[username][contest] = points
    
    for i in all_data:
        for j in all_data[i].copy():

            if contest not in j:
                all_data[contest] = points
            else:
                if points > all_data[i][contest]:
                    all_data[i][contest] = points
            print(all_data)
            
            
    command = input()
    
print(all_data)
