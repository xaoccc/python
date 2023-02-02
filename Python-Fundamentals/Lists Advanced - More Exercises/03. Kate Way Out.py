rows = int(input())
rows_list = []
kate_row = 0
kate_col = 0

for i in range(rows):
    current_row = input()
    if "k" in current_row:
        kate_row = i + 1
        kate_col = current_row.find("k") + 1
    rows_list.append(current_row)
print(kate_row)
print(kate_col)
