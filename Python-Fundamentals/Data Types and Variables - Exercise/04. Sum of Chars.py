chars_num = int(input())
ascii_sum = 0
for _ in range(chars_num):
  char_input = input()
  ascii_sum += ord(char_input)
print(f"The sum equals: {ascii_sum}")
