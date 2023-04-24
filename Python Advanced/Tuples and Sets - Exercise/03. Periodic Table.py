inputs = int(input())
all_elements = []
remove_list = []
for i in range(inputs):
    current_elements = input().split()
    if len(current_elements) != len(set(current_elements)):
        for el in current_elements:
            if current_elements.count(el) > 1:
                remove_list.append(el)
    all_elements += current_elements

if not remove_list:
    print(*set(all_elements), sep="\n")
else:
    print(*set(all_elements) - set(remove_list), sep="\n")
