letter_input = ""
message = ""
print_msg = ""
c_count = 0
n_count = 0
o_count = 0

while True:
    letter_input = input()
    if letter_input == "End":
        break
    if len(letter_input) > 1 or letter_input == " ":
        continue
#i is the decimal number of the ASCII code of the letter_input. Here we turn all inputs into digits
    i = ord(letter_input)
    if i == 99:
        c_count += 1
        if c_count == 1:
            i = 0
    elif i == 110:
        n_count += 1
        if n_count == 1:
            i = 0
    elif i == 111:
        o_count += 1
        if o_count == 1:
            i = 0
    if c_count >= 1 and n_count >= 1 and o_count >= 1:
        i = 32
        c_count = 0
        n_count = 0 
        o_count = 0
    if (97 <= i <= 122) or (65 <= i <= 90) or i == 32:
#Here we turn back all ASCII digits into text
        message += chr(i)
        if i == 32:
#Every message ends with a SPACE, so we add this condition, so the message is full and legit
            print_msg = message

print(print_msg)