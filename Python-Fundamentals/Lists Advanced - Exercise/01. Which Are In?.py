input_list1 = input().split(", ")
input_list2 = input()
final_list = []

for i in range(len(input_list1)):
    if input_list1[i] in input_list2:
        final_list.append(input_list1[i])
print(final_list)
