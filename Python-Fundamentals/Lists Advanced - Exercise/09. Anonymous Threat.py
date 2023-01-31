input_text = input().split()
command = input().split()

while command[0] != "3:1":
    merged = ""
    if command[0] == "merge":
        if int(command[1]) < 0:
            command[1] = 0
        if int(command[2]) >= len(input_text):
            command[2] = len(input_text) - 1
        for i in range(int(command[1]), int(command[2]) + 1):
            merged += input_text[i]
        input_text.insert(int(command[1]), merged)
        del input_text[int(command[1]) + 1 : int(command[2]) + 2]
    elif command[0] == "divide":
        element_to_divide = input_text[int(command[1])]
        divided_element = ""
        substring_len = len(element_to_divide) // int(command[2])
        
        diff = len(element_to_divide) % int(command[2])
        
        
        if diff == 0:
            for i in range(0, len(element_to_divide), substring_len):
                divided_element += element_to_divide[i : i + substring_len] + " "
        else:
            for i in range(0, len(element_to_divide), substring_len):
                if i == (len(element_to_divide) - diff) - substring_len:
                    divided_element += element_to_divide[i : ]
                    break
                else:
                    divided_element += element_to_divide[i : i + substring_len] + " "
        divided_element = divided_element.split()
        for i in range(len(divided_element) - 1, -1, -1):
            input_text.insert(int(command[1]) + 1, divided_element[i])    
        input_text.pop(int(command[1]))
    command = input().split()
print(" ".join(input_text))
