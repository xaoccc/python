n = int(input())
even = []
odd = []
negative = []
positive = []

for i in range(n):
  num = int(input())
  if num < 0:
    negative.append(num)
  if num >= 0:
    positive.append(num)
  if num % 2 == 0 or num == 0:
    even.append(num)
  if num % 2 != 0:
    odd.append(num)
command = input()
if command == "even":
  output = even
elif command == "odd":
  output = odd
elif command == "positive":
  output = positive
else:
  output = negative  
  
print(output)
