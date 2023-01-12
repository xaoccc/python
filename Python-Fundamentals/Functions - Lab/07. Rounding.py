def rounding(nums = input()):
#in 1 line we do 3 actions: 
#1. nums.split() makes the string into a list 
#2. eval(i) for i in nums turns all str elements into float
#3. round() formats them
    nums = [round(eval(i)) for i in nums.split()]
    return nums
print(rounding())
