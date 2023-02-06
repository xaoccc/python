nums = [int(i) for i in input().split()]
output = []
average_num = sum(nums) / len(nums)
for i in nums:
    if i > average_num:
        output.append(i)
if len(output) == 0:
    print("No")
else:
    output.sort()
    output.reverse()
    if len(output) > 5:
        del output[5: ]
    output = [str(i) for i in output]
    print(" ".join(output))
