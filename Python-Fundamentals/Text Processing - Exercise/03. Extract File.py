text_input = input().split("\\")
text_input[-1] = text_input[-1].split(".")
print(f"File name: {text_input[-1][0]}\nFile extension: {text_input[-1][1]}")
