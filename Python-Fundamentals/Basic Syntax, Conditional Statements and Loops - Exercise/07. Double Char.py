while True:
  double_string = ""
  string_input = input()
  if string_input == "End":
    break
  if string_input == "SoftUni":
    continue
  for i in range(len(string_input)):
    double_string += 2 * string_input[i]
  print(double_string)
