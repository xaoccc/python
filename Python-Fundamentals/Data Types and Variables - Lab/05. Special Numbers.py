num = input()
digits_sum = 0
for i in range(1, int(num) + 1):
  digits_sum = 0
  for j in range(len(str(i))):    
    digits_sum += int(str(i)[j])
  if digits_sum == 5 or digits_sum == 7 or digits_sum == 11:
    print(f"{i} -> True")
  else:
    print(f"{i} -> False")
