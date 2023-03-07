inputs_num = int(input())
for i in range(inputs_num):
    text_input = input()
    name = text_input[text_input.index("@") + 1 : text_input.index("|")]
    age = text_input[text_input.index("#") + 1 : text_input.index("*")]
    print(f"{name} is {age} years old.")
