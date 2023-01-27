text = input().split()
decoded_message = []

for i in range(len(text)):
    first_letter = ""
    remaining_letters = ""
    for j in range(len(text[i])):
        if text[i][j].isdigit():
            first_letter += text[i][j]
        else:
            remaining_letters += text[i][j]
    decoded_message.append(chr(int(first_letter)) + remaining_letters)
    if len(decoded_message[i]) > 2:
        decoded_message[i] = decoded_message[i][0] + decoded_message[i][-1] + decoded_message[i][2:-1] + decoded_message[i][1]
    
print(" ".join(decoded_message))
