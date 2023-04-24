matrix_size = [int(i) for i in input().split(", ")]
total = 0
all_data = []
for i in range(matrix_size[0]):
    row_data = [int(j) for j in input().split(", ")]
    total += sum(row_data)
    all_data.append(row_data)
print(total)
print(all_data)
