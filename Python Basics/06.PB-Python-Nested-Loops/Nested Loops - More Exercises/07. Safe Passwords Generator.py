a = int(input())
b = int(input())
max_pass_num = int(input())
pass_num = 0
i = 35
j = 64

for k in range(1, a + 1):
  symbol3 = str(k)
  k += 1
  if pass_num > max_pass_num - 1:
    break
  for l in range(1, b + 1):
    symbol4 = str(l)
    l += 1
    if i > 55:    
      i = 35
    if j > 96:
      j = 64
    print(chr(i) + chr(j) + symbol3 + symbol4 + chr(j) + chr(i), end="|")
    i += 1
    j += 1
    pass_num += 1
    if pass_num > max_pass_num - 1:
      break