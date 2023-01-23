pal_input_list = input().split()
pal_word = input()
pal_word_count = 0
pal_output_list = []

for word in pal_input_list:
    if word == pal_word:
        pal_word_count += 1
    
    if len(word) % 2 == 0:
        #there are 6 methods to reverse a string, we can also do it like this:
        #We can replace word[len(word) // 2:][::-1] with "".join(reversed(word[len(word) // 2:]))
        if word[:len(word) // 2] == word[len(word) // 2:][::-1]:
            pal_output_list.append(word)

    else:
        #here we can also use the other solution, using join() and reversed() 
        if word[:len(word) // 2] == word[(len(word) // 2) + 1:][::-1]:
            pal_output_list.append(word)

print(pal_output_list)
print(f"Found palindrome {pal_word_count} times")
