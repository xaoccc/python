def palindrome(text, idx):
    # If we find a char, which is not the same as the mirror char in the word, we end the loop
    if text[idx] != text[len(text) - idx - 1]:
        return f"{text} is not a palindrome"
    # If we check all chars and we do not find a non-palidrome char, we assume the word is a palindrome
    elif idx == len(text) - 1:
        return f"{text} is a palindrome"
    # Here we start checking the first and the last letter for each iteration. 
    return palindrome(text, idx + 1)
    
print(palindrome("abcba", 0)) 





# def palindrome(*args):
#     palindrome = True
#     for i in range(len(args[0]) // 2):
#         if args[0][i] != args[0][len(args[0]) - i -1]:
#             palindrome = False
#     if palindrome:
#         return f"{args[0]} is a palindrome"
#     else:
#         return f"{args[0]} is not a palindrome"
