nums = input().split()
stack = []
for i in range(len(nums)):
    stack.append(nums.pop())
print(*stack)
