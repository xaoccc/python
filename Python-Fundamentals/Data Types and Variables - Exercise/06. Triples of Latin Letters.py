char_num = int(input())

for i in range(0, char_num):
  for j in range(0, char_num):
    for k in range(0, char_num):
      print(f"{chr(97 + i) + chr(97 + j) + chr(97 + k)}")
