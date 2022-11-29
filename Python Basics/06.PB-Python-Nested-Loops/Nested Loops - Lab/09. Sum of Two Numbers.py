start = int(input())
end = int(input())
magic_num = int(input())
try_num = 0
num = 0

for i in range(start, end + 1):
  if num == magic_num:
    break
  for j in range(start, end + 1):
    num = i + j
    try_num += 1
    if num == magic_num:
      print(f"Combination N:{try_num} ({i} + {j} = {magic_num})")
      break
if num != magic_num:
  print(f"{try_num} combinations - neither equals {magic_num}")