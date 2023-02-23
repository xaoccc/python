student_data = input().split(":")
all_data = {}

while True:
    if len(student_data) == 1:
        if "_" in student_data[0]:
            student_data[0] = student_data[0].replace("_", " ")
        data_filter = student_data[0]
        break

    student_name = student_data[0]
    student_id = student_data[1]
    course = student_data[2]
    if course not in all_data:
        all_data[course] = []
    all_data[course].append(f"{student_name} - {student_id}")
    
    student_data = input().split(":")
    
for i in all_data[data_filter]:
    print(i)
