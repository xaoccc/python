def max_min_sum(nums_input):
    return f"The minimum number is {min(nums_input)}\nThe maximum number is {max(nums_input)}\nThe sum number is: {sum(nums_input)}"
print(max_min_sum([int(i) for i in input().split()]))
