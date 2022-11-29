fails_num = int(input())
fails = 0
try_num = 0
sum_grades = 0

while fails < fails_num:
    problem = input()
    if problem == "Enough":
        print(f"Average score: {avg_grade:.2f}")
        print(f"Number of problems: {try_num}")
        print(f"Last problem: {last_problem}")
        break
    grade = int(input())
    if grade <= 4:
        fails += 1
    try_num += 1
    sum_grades += grade
    avg_grade = sum_grades / try_num
    last_problem = problem

if fails == fails_num:
    print(f"You need a break, {fails} poor grades.")