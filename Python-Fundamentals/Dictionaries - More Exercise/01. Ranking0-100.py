command = input()
all_data = {}
contest_data = {}

while command != "no more time":
    command = command.split(" -> ")
    username = command[0]
    contest = command[1]
    points = int(command[2])
    if username not in all_data:
        all_data[username] = {}
        all_data[username][contest] = points
        
    if contest not in contest_data:
        contest_data[contest] = {}
        contest_data[contest][username] = points
    
    for i in all_data.copy():
        for j in all_data[i].copy():
            if contest not in j:
                all_data[username][contest] = points
            else:
                if points > all_data[i][j]:
                    all_data[i][j] = points
                    break
    
    for i in contest_data.copy():
        for j in contest_data[i].copy():
            if username not in j:
                contest_data[contest][username] = points
            else:
                if points > contest_data[i][j]:
                    contest_data[i][j] = points
                    break       
            
    command = input()
sorted_data = {}

for i in all_data: 
    sorted_data = dict(sorted(all_data[i].items(), key=lambda y:y[1], reverse=True))        
    for (key, value) in sorted_data.items():
        print(f"#{i}  {key} -> {value}") 
    
print(contest_data)

for i in contest_data: 
    sorted_data = dict(sorted(contest_data[i].items(), key=lambda y:y[1], reverse=True))        
    for (key, value) in sorted_data.items():
        print(f"#{i}  {key} -> {value}") 
