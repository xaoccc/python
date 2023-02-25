command = input()
registered_students = {}

while command != "end":
    command = command.split(" : ")
    course = command[0]
    student_name = command[1]
    if course not in registered_students:
        registered_students[course] = []
    registered_students[course].append(student_name)
    command = input()
for (key, value) in registered_students.items():
    print(f"{key}: {len(value)}")
    for i in value:
        print(f"-- {i}")
