command = input()
exams_info = {}
submissions_info = {}

while command != "exam finished":
    command = command.split("-")
    username = command[0]
    if len(command) == 3:
        language = command[1]
        points = int(command[2])

        if language not in submissions_info:
            submissions_info[language] = 0
        submissions_info[language] += 1

        if username not in exams_info:
            exams_info[username] = []
            exams_info[username].append(language)
            exams_info[username].append(points)

        if username in exams_info and points > exams_info[username][1]:
            exams_info[username][1] = points

    else:
        exams_info.pop(username)

    command = input()
print("Results:")
for (username, points) in exams_info.items():
    print(f"{username} | {points[1]}")
print("Submissions:")
for (key, value) in submissions_info.items():
    print(f"{key} - {value}")

