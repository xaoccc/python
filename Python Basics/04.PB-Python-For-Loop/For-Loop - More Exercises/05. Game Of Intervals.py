#user input
turns = int(input())
num_group1 = 0
num_group2 = 0
num_group3 = 0
num_group4 = 0
num_group5 = 0
num_group6 = 0
num_sum = 0
pts = 0

#logic
for i in range (1, turns + 1) :
    number = int(input())
    if 0 <= number <= 9 :
        pts += number * 0.2
        num_group1 += 1
    elif 9 < number <= 19 :
        pts += number * 0.3
        num_group2 += 1
    elif 19 < number <= 29 :
        pts += number * 0.4
        num_group3 += 1
    elif 29 < number <= 39 :
        pts += 50
        num_group4 += 1
    elif 39 < number <= 50 :
        pts += 100
        num_group5 += 1
    if number < 0 or number > 50 : 
        pts = pts / 2
        num_group6 += 1

#print output
print(f"{pts:.2f}")
print(f"From 0 to 9: {(num_group1 * 100 / turns):.2f}%")
print(f"From 10 to 19: {(num_group2 * 100 / turns):.2f}%")
print(f"From 20 to 29: {(num_group3 * 100 / turns):.2f}%")
print(f"From 30 to 39: {(num_group4 * 100 / turns):.2f}%")
print(f"From 40 to 50: {(num_group5 * 100 / turns):.2f}%")
print(f"Invalid numbers: {(num_group6 * 100 / turns):.2f}%")