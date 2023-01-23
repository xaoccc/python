employees = input().split()
h_factor = int(input())
happy_people_count = 0
total_happiness = 0

for employee in employees:
    total_happiness += (int(employee) * h_factor)
average_happiness = total_happiness / len(employees)

for employee in employees:
    if int(employee) * h_factor >= average_happiness:
        happy_people_count += 1
        
if happy_people_count >= len(employees) / 2:
    print(f"Score: {happy_people_count}/{len(employees)}. Employees are happy!")
else:
    print(f"Score: {happy_people_count}/{len(employees)}. Employees are not happy!")
