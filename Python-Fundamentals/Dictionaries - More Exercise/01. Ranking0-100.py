command_one = input()
contest_entry_info = {}
students_info = {}
students_grades = {}

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
            students_grades[contest] = int(points)
            students_info[username] = students_grades

    command_two = input()
print(students_info)

total = {}

for i in students_info:
    sorted_data = dict(sorted(students_info[i].items(), key=lambda x:x[1], reverse=True))
    if i not in total:
        total[i] = sum(sorted_data.values())

max_grade = max(total, key=total.get)      
print(f"Best candidate is {max_grade} with {max(total.values())} points\nRanking:")

for i in students_info:
    print(i)
    sorted_data = dict(sorted(students_info[i].items(), key=lambda x:x[1], reverse=True))
    for (key, value) in sorted_data.items():
        print(f"# {key} -> {value}")
