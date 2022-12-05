first_num = int(input())
second_num = int(input())
third_num = int(input())

max_num = first_num
if second_num > max_num and second_num > third_num:
  max_num = second_num
elif third_num > max_num and third_num > second_num:
  max_num = third_num

print(max_num)
