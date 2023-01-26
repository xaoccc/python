students_num = int(input())
lectures_num = int(input())
bonus = int(input())
max_bonus = 0
max_bonus_att = 0

for i in range(students_num):
    attend_num = int(input())
    current_bonus = attend_num / lectures_num * (5 + bonus)
    if current_bonus > max_bonus:
        max_bonus = current_bonus
        max_bonus_att = attend_num
print(f"Max Bonus: {round(max_bonus)}.")
print(f"The student has attended {max_bonus_att} lectures.")
