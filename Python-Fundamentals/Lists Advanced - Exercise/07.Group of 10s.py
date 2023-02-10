#We split the input into a list with integers
nums = [int(i) for i in input().split(", ")]
#Then we find the total number of groups, according to the biggest number in the list
if max(nums) % 10 == 0:
    nums_groups = max(nums) // 10
else:
    nums_groups = max(nums) // 10 + 1
#here we store the results
groups_list = [[]]

for i in range(nums_groups):
    #For each iteration of the nested loop we need a fresh empty list, this list will contain the result of each group: 10s, 20s, etc. so 
    #the first current_list will be groups_list[0], the second current_list will be groups_list[1] and so on
    current_list = []
    for j in range(len(nums)):
        #Each groups_list[i] / current_list (both are the same thing) will be filled here. We write nums[j] = -1, so we make sure we cannot use the same element of nums[] twice
        if nums[j] // ((i+1) * 10) == 0 or nums[j] / ((i+1) * 10) == 1:
            current_list.append(nums[j])
            nums[j] = -1
    #After each loop of nums, we add one element(which is a list) to groups_list until we fill the info for all groups
    groups_list.append(current_list)

#Now that we have all groups, stored in lists inside the list nums_groups, we simply print each element for each group
for i in range(1, nums_groups + 1):  
    print(f"Group of {i}0\'s: {groups_list[i]}")

    
# numbers = [int(i) for i in input().split(", ")]
# groups = 0
# while numbers:
#     groups += 10
#     print_list = [i for i in numbers if i <= groups]
#     numbers = [i for i in numbers if i > groups]
#     print(f"Group of {groups}'s: {print_list}")
