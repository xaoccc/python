def loading_bar(num_input):
    if num_input != 100:
        return str(num_input) + "% [" + "%" * (num_input // 10) + "." * (10 - (num_input // 10)) + "]""\nStill loading..."
    else:
        return "100% Complete!\n[" + 10 * "%" + "]"
print(loading_bar(int(input()))) 
