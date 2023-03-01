command = input()
all_data, users_data, contest_data, sorted_data = {}, {}, {}, {}

while command != "no more time":
    username, contest, points = command.split(" -> ")
    points = int(points)
    if username not in all_data:
        all_data[username] = {contest: points}
    else:
        if contest not in all_data[username] or points > all_data[username][contest]:
            all_data[username][contest] = points
    if contest not in contest_data:
        contest_data[contest] = {username: points}
    else:
        if username not in contest_data[contest] or points > contest_data[contest][username]:
            contest_data[contest][username] = points
    command = input()

for i in contest_data: 
    sorted_data, el = dict(sorted(contest_data[i].items(), key=lambda y: (-y[1], y[0]))), 1
    print(f"{i}: {len(contest_data[i])} participants")
    for (key, value) in sorted_data.items():
        print(f"{el}. {key} <::> {value}") 
        el += 1
        
for i in all_data:
    users_data[i] = sum(all_data[i].values())

sorted_data, el = dict(sorted(users_data.items(), key=lambda y: (-y[1], y[0]))), 1
print("Individual standings:")
for i in sorted_data:
    print(f"{el}. {i} -> {sorted_data[i]}") 
    el += 1
