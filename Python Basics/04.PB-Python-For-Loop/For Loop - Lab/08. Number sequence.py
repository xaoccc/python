#input
n = int(input())
biggest_number = -10000000
lowest_number = 10000000

#logic
for i in range (0, n):
    current_num = int(input())
    if current_num >= biggest_number :
        biggest_number = current_num
    if current_num < lowest_number :
        lowest_number = current_num

#output
print(f"Max number: {biggest_number}")
print(f"Min number: {lowest_number}")