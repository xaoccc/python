text_input = input()
print(text_input[0], end="")
for i in range(1, len(text_input)):
    if text_input[i] != text_input[i-1]:
        print(text_input[i], end="")