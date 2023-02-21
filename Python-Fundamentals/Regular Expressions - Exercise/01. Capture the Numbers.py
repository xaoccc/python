import re
input_data = []
pattern = "\d+"

while True:
    text_input = input()
    input_data.append(text_input)
    matches = re.findall(pattern, " ".join(input_data))
print(" ".join(matches))
