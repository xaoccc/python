start = ord(input())
end = ord(input())
text_input = input()
result = 0
for char in text_input:
    if start < ord(char) < end:
        result += ord(char)
print(result)
