string = input()
output = string.split(" ")
for i in range(len(output)):
  output[i] = int(output[i])
  output[i] *= -1
print(output)
