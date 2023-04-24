matrix_size = int(input())
all_data = []
for i in range(matrix_size):
    row_data = [int(j) for j in input().split(", ") if int(j) % 2 == 0]
    all_data.append(row_data)
print(all_data)
