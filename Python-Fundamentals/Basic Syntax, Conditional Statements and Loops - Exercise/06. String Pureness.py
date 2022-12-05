strings_num = int(input())
for i in range(strings_num):
  string = input()
  if string.find('.') == -1 and string.find(',') == -1 and string.find('_') == -1:
    print(f"{string} is pure.")
  else:
    print(f"{string} is not pure!")
