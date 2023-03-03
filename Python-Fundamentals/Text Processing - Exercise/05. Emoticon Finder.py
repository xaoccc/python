text_input = input()

for i in range(len(text_input)):
    if text_input[i] == ":":
        print(f"{text_input[i]}{text_input[i+1]}")