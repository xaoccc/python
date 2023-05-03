def palindrome(*args):
    palindrome = True
    for i in range(len(args[0]) // 2):
        if args[0][i] != args[0][len(args[0]) - i -1]:
            palindrome = False
    if palindrome:
        return f"{args[0]} is a palindrome"
    else:
        return f"{args[0]} is not a palindrome"
