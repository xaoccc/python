text = input()
parentness = []
for i in range(len(text)):
    if text[i] == "(":
        parentness.append(i)
    elif text[i] == ")":
        start_index = parentness.pop()
        print(text[start_index:i+1])
