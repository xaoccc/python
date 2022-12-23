nums_list = input()
biggest_num = int(input())
nums_list = nums_list.split(" ")
sorted_nums = []
nums_list_int = []
final_list = []
biggest_str = ""
for _ in range(len(nums_list)):
  sorted_nums.append(int(nums_list[_]))
  nums_list_int.append(int(nums_list[_]))
sorted_nums = sorted(sorted_nums)

biggest = sorted_nums[-(len(nums_list) - biggest_num):]

for i in range(len(nums_list)):
  if biggest.count(nums_list_int[i]) > 0:
    final_list.append(nums_list_int[i])
for j in range(len(biggest)):
  if j != len(biggest) - 1:
    biggest_str += str(final_list[j]) + ", "
  else:
    biggest_str += str(final_list[j])
print(biggest_str)
