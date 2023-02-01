input_list = [int(i) for i in input().split()]
new_list = []
def even_nums(num):
    if num % 2 == 0:
        return 1

result = filter(even_nums, input_list)

for num in result:
     new_list.append(num)
print(new_list)
