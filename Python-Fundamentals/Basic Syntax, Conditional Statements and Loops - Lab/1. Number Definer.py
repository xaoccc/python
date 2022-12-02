num = float(input())
output = ""
if num == 0:
  output = "zero"
elif num < 0:
  output = "negative"
  if num > -1:
    output = "small " + output
  elif num < -1000000:
    output = "large " + output
else:
  output = "positive"
  if num < 1:
    output = "small " + output
  elif num > 1000000:
    output = "large " + output

print(output)
