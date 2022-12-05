string_one = input()
string_two = input()
for i in range(len(string_one)):
  #Find only unique strings
  if string_one[i] != string_two[i]:
    #This is the formula to replace the exact char string_one[i] with another char string_two[i]
    #It can be easily mistaken with replace(char1, char2, number_of_replaces), but in this problem this will not work, because it will replace the first possible char
    #instead of exact char on position i
    string_one = string_one[:i] + string_two[i] + string_one[i + 1:]
    print(string_one)
