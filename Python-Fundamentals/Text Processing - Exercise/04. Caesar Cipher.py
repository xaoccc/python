text_input = input()
result = ""
for i in text_input:
    result += chr(ord(i) + 3)
print(result)