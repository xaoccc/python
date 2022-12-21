input_lines = int(input())
balanced = "BALANCED"
open_brackets = 0
close_brackets = 0

for i in range(input_lines):
  input_char = input()
  if input_char.count("(") > 1 or input_char.count(")") > 1 or (input_char == ")" and open_brackets == 0):
    balanced = "UNBALANCED"
    break
  if input_char == "(":
    open_brackets += 1
    balanced = "UNBALANCED"
  if input_char == ")" and open_brackets == 1:
    balanced = "BALANCED"
    open_brackets = 0   

print(balanced)
