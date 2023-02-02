def char_range(char_one, char_two):
    char_list = []
    for i in range(ord(char_one) + 1, ord(char_two)):
        char_list.append(chr(i))
    return (" ").join(char_list)
print (char_range(input(), input()))
