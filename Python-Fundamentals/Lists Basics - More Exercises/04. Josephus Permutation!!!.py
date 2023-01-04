#For iterating through a list with specific interval, a while loop is preferrable and we definitely need a break condition and the correct iterator


soldiers_list = input()
num = int(input())
soldiers_list = soldiers_list.split(" ")
soldiers_list_int = [eval(i) for i in soldiers_list]
#Solution for list output: new_list = []
i = 0
new_string = "["
while len(soldiers_list_int) != 0:
  #The most important part here is the iterator. if x < y, x % y = x, if x = y, x % y = 0.
    i = (i + num - 1) % len(soldiers_list_int)
    new_string += str(soldiers_list_int[i]) + ","
#Solution for list output: new_list.append(soldiers_list_int[i])
#Here we remove each used element from the first list. This is used for the break condition.
    del soldiers_list_int[i]
#If we need output with no whitespaces, we need a string:
new_string = new_string.strip(new_string[-1])
print(new_string + "]")
