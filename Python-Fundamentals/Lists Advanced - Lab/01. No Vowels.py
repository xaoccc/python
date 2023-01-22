input_text = input()
skip_letters = ["a", "e", "o", "u", "i", "A", "E", "O", "U", "I"]
output_text = []

for i in input_text:
    if i not in skip_letters:
        output_text.append(i)
print("".join(output_text))
