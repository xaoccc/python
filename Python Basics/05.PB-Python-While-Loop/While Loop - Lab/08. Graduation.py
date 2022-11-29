student_name = input()
#here grade is 1, because of the first check on line 11
grade = 1
sum_mark = 0
broken = 0

while True:
#Student mark input
    mark = float(input())
#Mark check for grade 1 and above, if grade was 0, there is no logic in having a mark (ocenka)
    if mark < 4:
        broken += 1
#The second "if" is indented and checking for the first breakpoint, if the student is not passing to the next grade (broken == True), we must return to the beginning of the loop ( O4CHENIKAT POVTARIA) and we don't count a new grade!!! If there are 2 fails, the student is excluded, the loop finishes with 1st breakpoint.
        if broken >= 2:
            break
        continue
#Here we count the grades until 12
    grade += 1
    sum_mark += mark
#And here is the 2nd breakpoint, where the student gets to 12-th grade. Very important - in the beginning grade = 1 and sum_mark = 0, but here we have grade = 2 and the mark for grade 1, here is the moment the student finishes the grade and when grade becomes 13 - the 2nd breakpoint, we already have all 12 marks for each class and the student finishes school and we exit the loop
    if grade > 12:
        break
#Outputs
if broken >= 2:
    print(f"{student_name} has been excluded at {grade} grade")
else:
    print(f"{student_name} graduated. Average grade: {sum_mark / 12:.2f}")