passwords = {}
users_data = {}
contest_data = {}
total_score = {}

command = input()
while command != "end of contests":
    command = command.split(":")
    contest = command[0]
    password = command[1]
    if contest not in passwords:
        passwords[contest] = password
    command = input()

contest_input = input()
while contest_input != "end of submissions":
    contest_data = {}
    contest_input = contest_input.split("=>")
    if len(contest_input) == 4:
        contest = contest_input[0]
        password = contest_input[1]
        username = contest_input[2]
        points = int(contest_input[3])
        if contest in passwords and password == passwords[contest]:
            contest_data[contest] = points
            if username not in users_data:
                users_data[username] = contest_data
            else:
                if users_data[username][contest] < points:
                    users_data[username][contest] = points
                    
        print(contest_data)
        print(users_data)
              
        contest_input = input()
    else:
        contest_input = input()

for user in users_data:
    for contests in user:
        total_score[user] = sum(contests.values())
        
print(total_score)
