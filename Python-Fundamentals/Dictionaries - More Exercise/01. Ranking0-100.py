passwords = {}
users_data = {}
contest_data = {}
total_score = {}
sorted_data = {}

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
                if contest not in users_data[username]:
                    users_data[username][contest] = points
                elif users_data[username][contest] < points:
                    users_data[username][contest] = points
                    
        contest_input = input()
    else:
        contest_input = input()

for (user, contestdata) in users_data.items():
    total_score[user] = sum(contestdata.values())

best_score = max(total_score.values())
best_user = list(total_score.keys())[list(total_score.values()).index(best_score)]
print(f"Best candidate is {best_user} with total {best_score} points.")

myKeys = list(users_data.keys())
myKeys.sort()
sorted_data = {i: users_data[i] for i in myKeys}

for i in sorted_data:
    sorted_data[i] = dict(sorted(sorted_data[i].items(), key=lambda x: x[1], reverse=True)) 

print("Ranking:")
for (user, result) in sorted_data.items():
    print(user)
    for (contest, points) in result.items():
        print(f"# {contest} -> {points}")
