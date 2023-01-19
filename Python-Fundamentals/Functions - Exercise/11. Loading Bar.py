def loading_bar(num_input = int(input())):
    num_input_ = num_input // 10
    if num_input != 100:
        print(str(num_input) + "% [" + "%" * num_input_ + "." * (10 - num_input_) + "]")
        print("Still loading...")
    else:
        print("100% Complete!")
        print("[" + 10 * "%" + "]")
loading_bar() 
