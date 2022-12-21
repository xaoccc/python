n = int(input())
word = input()
strings = []
new_list = []

for i in range(n):
  current_string = input()
  strings.append(current_string)
  if current_string.count(word) > 0:
    new_list.append(current_string)
  
print(strings)
print(new_list)
