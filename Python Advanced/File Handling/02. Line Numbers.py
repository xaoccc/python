try:
    file = open("text.txt", "r")
except FileNotFoundError:
    print("Path not correct or file not found!")

symbols = ["-", ",", ".", "!", "?", "'"]
text = file.readlines()

result = open('output.txt', 'w')
i = 1
for line in text:
    line = line.replace("\n", "")
    letters, punctuation_marks = 0, 0
    for char in line:
        if char.isalpha():
            letters += 1
        elif char in symbols:
            punctuation_marks += 1
    result.write(f"Line {i}: {line} ({letters})({punctuation_marks})\n")

    i += 1
