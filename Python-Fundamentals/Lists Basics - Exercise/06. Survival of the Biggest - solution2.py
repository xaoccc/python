from itertools import chain
nums_list = input()
biggest_num = int(input())
nums_list = nums_list.split(" ")
sorted_nums = []
for i in range(len(nums_list)):
  sorted_nums.append(int(nums_list[i]))
sorted_nums = sorted(sorted_nums)
for j in chain(range(0, len(nums_list)), range(len(nums_list), -1, -1)):
    if j > len(nums_list) - 1:
        continue
    if int(nums_list[j]) < sorted_nums[biggest_num]:
        nums_list.remove(nums_list[j])
    
print(", ".join(nums_list))
