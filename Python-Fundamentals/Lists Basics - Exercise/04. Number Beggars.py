#input
int_string = input()
beggars_num = int(input())
#Converting the input into a list
int_string = int_string.split(", ")
#Creating a list to store the final data
final_list = []
new_list_element = 0

#logic
#We need two nested loops - one to iterate and sum each beggar profit and anouther one - to append each sum into the final list
for i in range(0, beggars_num + 1):
  final_list.append(new_list_element)
  new_list_element = 0
  for j in range(0, (len(int_string) // beggars_num) + 1):
    if i + beggars_num * j < len(int_string):
      new_list_element += int(int_string[i + beggars_num * j]) 
    else:
        break
#because we added the first element in the beginning, now we need to delete it    
del final_list[0]  
  
print(final_list)
