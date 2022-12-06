#since we have to sort, we need a string
num = input()

#Strings cannot be sorted, so we need a list
num_list = []

#Inserting all digits from the number into the list
for i in range(len(num)):
  num_list.append(num[i])
  
#Now we can sort the list
num_list.sort()

#And turn it into a string
largest_num = "".join(num_list)

#Now we have the smallest number, all we have to do is reverse the string and get the largest number and don't forget to turn it into an int
print(int(largest_num[::-1]))
