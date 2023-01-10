from itertools import chain

#input
nums_list = input()
biggest_num = int(input())

#logic
#create one list from the input and one - for sorting, where we keep the sorted input, created with sorted(), eval() and a for loop
nums_list = nums_list.split(" ")
sorted_nums = sorted([eval(i) for i in nums_list])

#A little confusing, the output variable is the altered input variable
#Here we iterate the list from the beginning to the end and backwards. chain() seems to be very useful for this
for j in chain(range(0, len(nums_list)), range(len(nums_list), -1, -1)):
#here we make sure we do not receive an index_out_of_range error:
    if j > len(nums_list) - 1:
        continue
    if int(nums_list[j]) < sorted_nums[biggest_num]:
        nums_list.remove(nums_list[j])
        
#output - should be a string 
print(", ".join(nums_list))
