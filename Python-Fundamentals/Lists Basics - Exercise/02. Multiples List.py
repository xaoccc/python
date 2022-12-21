factor = int(input())
count = int(input())
nums_list = []
for i in range(factor, factor * count + 1, factor):
  nums_list.append(i)
print(nums_list)
