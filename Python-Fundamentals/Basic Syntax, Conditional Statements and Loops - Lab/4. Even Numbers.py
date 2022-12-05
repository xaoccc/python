num_count = int(input())
even_num_count = 0
for i in range(num_count):
  num = int(input())
  if num % 2 != 0:
    print(f"{num} is odd!")
    break
  else:
    even_num_count += 1
if even_num_count == num_count:
  print("All numbers are even.")
