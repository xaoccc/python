lines_num = int(input())
capacity = 255
liters_total = 0

for i in range(lines_num):
  liters = int(input())
  capacity -= liters 
  if capacity < 0:
    capacity += liters
    print("Insufficient capacity!")
    continue
  liters_total += liters
  if liters_total > 255:
    liters_total -= liters    

print(liters_total)
