string = input()
output = []
for i in range(len(string)):
  if 64 < ord(string[i]) < 91:
    output.append(i)
print(output)
