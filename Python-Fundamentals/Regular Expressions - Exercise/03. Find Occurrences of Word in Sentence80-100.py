import re
text_input = input().lower()
string_check = input().lower()
text_input = re.sub(r'[\W_]', ' ', text_input)
text_input = text_input.split()
print(text_input.count(string_check))
