num_list = input()
num_list = num_list.split()

for i in range(len(num_list)):
    num_list[i] = abs(float(num_list[i]))
print(num_list)
