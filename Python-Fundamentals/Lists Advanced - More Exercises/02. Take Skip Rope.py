input_str = input()
digits_str, letters_str, take_list, skip_list = "", "", [], []
hidden_message = ""
total_chars_checked = 0

#Create two strings(we can do the same with lists) - 1st - for the digits and 2nd - for all other chars
for i in range(len(input_str)):
    if input_str[i].isdigit():
        digits_str += input_str[i]
    else:
        letters_str += input_str[i]

#Divide the digits string into 2 new lists - take_list and skip_list
for i in range(len(digits_str)):
    if i % 2 == 0:
        take_list.append(int(digits_str[i]))
    else:
        skip_list.append(int(digits_str[i]))

#Until we have any chars to add in the secret message "range(len(take_list))" we add chars and count the checked characters -> taken + skipped      
for i in range(len(take_list)):
    hidden_message += letters_str[total_chars_checked : total_chars_checked + take_list[i]]
    total_chars_checked += take_list[i] + skip_list[i]

print(hidden_message)
