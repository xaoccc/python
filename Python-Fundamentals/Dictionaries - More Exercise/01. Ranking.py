command_one = input()
contest_entry_info = {}
students_info = {}

while command_one != "end of contests":
    command_one = command_one.split(":")
    contest = command_one[0]
    password = command_one[1]
    if contest not in contest_entry_info:
        contest_entry_info[contest] = password
    command_one = input()

command_two = input()

while command_two != "end of submissions":
    command_two = command_two.split("=>")
    contest = command_two[0]
    if contest in contest_entry_info and len(command_two) == 4:
        password = command_two[1]
        if password in contest_entry_info[contest]:
            username = command_two[2]
            points = command_two[3]
            if username not in students_info:
                students_info[username] = []
            students_info[username].append([contest, int(points)])

    command_two = input()
print(contest_entry_info)
print(students_info)

for (key, value) in students_info.items():
    for i in range(len(value)):


print(f"Best candidate is {thebest} with total {max(points_list)} points.")