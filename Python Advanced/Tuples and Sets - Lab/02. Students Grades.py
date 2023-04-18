grades_num = int(input())
total_grades = {}

for i in range(grades_num):
    grade = tuple(input().split())
    if grade[0] not in total_grades:
        total_grades[grade[0]] = [float(grade[1])]
    else:
        total_grades[grade[0]].append(float(grade[1]))
for student, grade in total_grades.items():
    print(f"{student} ->", end="")
    for i in grade:
        print(f" {i:.2f}", end="")
    print(f" (avg: {sum(grade) / len(grade):.2f})")
