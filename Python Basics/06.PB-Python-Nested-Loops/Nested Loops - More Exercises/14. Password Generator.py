num1 = int(input())
num2 = int(input())

for i in range(1, num1 + 1):
  char_1 = i
  for j in range(1, num1 + 1):
    char_2 = j
    for k in range(97, 97 + num2):
      char_3 = chr(k)
      for l in range(97, 97 + num2):
        char_4 = chr(l)
        for m in range(1, num1 + 1):
          if m <= i or m <= j:
            continue
          char_5 = m
          print(f"{char_1}{char_2}{char_3}{char_4}{char_5}", end=" ")