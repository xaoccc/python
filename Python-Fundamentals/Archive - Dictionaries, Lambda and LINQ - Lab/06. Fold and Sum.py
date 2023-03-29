nums = [int(i) for i in input().split()]

list1 = nums[len(nums) // 4 : len(nums) // 2]
list2 = nums[ :len(nums) // 4 ]
list3 = nums[len(nums) // 2 : len(nums) * 3 // 4]
list4 = nums[-len(nums) // 4: ]
result1 = []
result2 = []
for i in range(len(nums) // 4):
    result1.append(list2[i] + list1[(len(nums) // 4) - 1 - i])
    result2.append(list3[i] + list4[(len(nums) // 4) - 1 - i])
result1.reverse()
result = result1 + result2
print(*result)
