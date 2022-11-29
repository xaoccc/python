men_num = int(input())
women_num = int(input())
tables_num = int(input())
dates_count = 0

for i in range (1, men_num + 1):  
  for j in range (1, women_num + 1):
    dates_count += 1
    if dates_count > tables_num:
      break
    else:
      print(f"({i} <-> {j})", end=" ")