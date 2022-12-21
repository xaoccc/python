int_string = input()
beggars_num = int(input())
int_string = int_string.split(", ")
final_list = []
new_list_element = 0

for i in range(0, beggars_num + 1):
  final_list.append(new_list_element)
  new_list_element = 0
  for j in range(0, (len(int_string) // beggars_num) + 1):
    if i + beggars_num * j < len(int_string):
      new_list_element += int(int_string[i + beggars_num * j]) 
    else:
        break
    
del final_list[0]  
  
print(final_list)
