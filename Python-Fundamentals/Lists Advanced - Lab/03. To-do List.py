command = input()
#Create the output list to put the data in
to_do = []

#Fill in the list with all commands
while command != "End":
    to_do.append(command)
    command = input()

#Now that we have the to-do list, we just have to sort it, so we turn the first part into a digit and then we sort it
for i in range(len(to_do)):
    to_do[i] = to_do[i].split("-")
    to_do[i][0] = int(to_do[i][0])
to_do = sorted(to_do)

#Now we have a sorted list, so we just remove the int in from of every action, using pop()
for i in range(len(to_do)):
    to_do[i].pop(0)
    #Because we have lists inside the list and we need strings inside the list, we have to use join() for each of the lists
    to_do[i] = "".join(to_do[i])
    
print(to_do)
