students_num = int(input())
students_data = {}

for i in range(students_num):
    student_name = input()
    student_grade = float(input())
    if student_name not in students_data:
        students_data[student_name] = []
    students_data[student_name].append(student_grade)

for (key, value) in students_data.items():
    average_grade = sum(value) / len(value)
    if average_grade >= 4.50:
        print(f"{key} -> {average_grade:.2f}")
