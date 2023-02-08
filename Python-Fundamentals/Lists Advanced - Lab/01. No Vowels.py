input_text = input()
skip_letters = ["a", "e", "o", "u", "i", "A", "E", "O", "U", "I"]
output_text = [i for i in input_text if i not in skip_letters]
print("".join(output_text))
