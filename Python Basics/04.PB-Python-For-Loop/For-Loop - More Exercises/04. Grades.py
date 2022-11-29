#user input
stud_num = int(input())
stud_grade1 = 0
stud_grade2 = 0
stud_grade3 = 0
stud_grade4 = 0
grade_sum = 0

#logic
for stud in range (1, stud_num + 1) :
    stud_grade = float(input())
    if 2 <= stud_grade < 3 :
        stud_grade1 += 1
    elif 3 <= stud_grade < 4 :
        stud_grade2 += 1
    elif 4 <= stud_grade < 5 :
        stud_grade3 += 1
    elif stud_grade >= 5 :
        stud_grade4 += 1
    grade_sum += stud_grade
avg_grade = grade_sum / stud_num

#print output
print(f"Top students: {(stud_grade4 * 100/ stud_num):.2f}%")
print(f"Between 4.00 and 4.99: {(stud_grade3 * 100/ stud_num):.2f}%")
print(f"Between 3.00 and 3.99: {(stud_grade2 * 100/ stud_num):.2f}%")
print(f"Fail: {(stud_grade1 * 100/ stud_num):.2f}%")
print(f"Average: {avg_grade:.2f}")
