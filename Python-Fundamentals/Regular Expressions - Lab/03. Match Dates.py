import re
text_input = input()
pattern = r'(\d{2}([\-\.\/])[A-Z][a-z]{2}\2\d{4})\b'
result = re.findall(pattern, text_input)
for i in range(len(result)):
    print(f"Day: {result[i][0][ :2]}, Month: {result[i][0][3:6]}, Year: {result[i][0][-4: ]}")
