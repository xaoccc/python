efficiency_one = int(input())
efficiency_two = int(input())
efficiency_three = int(input())
total_efficiency = efficiency_one + efficiency_two + efficiency_three
students_num = int(input())
time_needed = 0
while students_num > 0:
    students_num -= total_efficiency
    time_needed += 1

    if time_needed % 4 == 0:
        time_needed += 1

print(f"Time needed: {time_needed}h.")
