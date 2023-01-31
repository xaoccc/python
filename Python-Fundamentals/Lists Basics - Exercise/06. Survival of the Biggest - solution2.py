nums_list = [int(i) for i in input().split()]
biggest_num = int(input())

for i in range(biggest_num):
    smallest = min(nums_list)
    nums_list.remove(smallest)
    
nums_list = [str(i) for i in nums_list]
print(", ".join(nums_list))
