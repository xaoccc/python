#user input
n = int(input())

#variables - one variable for the current input and five variables for each group
current_num = 0
num_group_one = 0
num_group_two = 0
num_group_three = 0
num_group_four = 0
num_group_five = 0

#logic
#reading the number of inputs
for i in range (0, n) :
    current_num = int(input())
    if current_num < 200 :
#counting each input for each group. n value should be equal to the sum of all num_group variables.
        num_group_one += 1
    elif current_num < 400 :
        num_group_two += 1
    elif current_num < 600 :
        num_group_three += 1
    elif current_num < 800 :
        num_group_four += 1
    elif current_num >= 800 :
        num_group_five += 1

#print output
print(f"{(num_group_one*100/n):.2f}%")
print(f"{(num_group_two*100/n):.2f}%")
print(f"{(num_group_three*100/n):.2f}%")
print(f"{(num_group_four*100/n):.2f}%")
print(f"{(num_group_five*100/n):.2f}%")