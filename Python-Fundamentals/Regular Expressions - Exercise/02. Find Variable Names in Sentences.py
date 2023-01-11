text_input = input()
text_input_list = text_input.split(" ")
variable_name = ""
text_output_list = []
print(text_input_list)

for i in range(len(text_input_list)):
    if text_input_list[i].find('_') == 0 and text_input_list[i].rfind('_') == 0 and (text_input_list[i][1:].isalnum() == True or text_input_list[i][1:].isalpha() == True or text_input_list[i][1:].isdigit() == True):

        text_input_list[i] = text_input_list[i][1:]
        text_output_list.append(text_input_list[i])

print(",".join(text_output_list)) 
