gifts_list = input()
gifts_list = gifts_list.split(" ")
command = input()

while True:
  command = command.split(" ")
  if command.count("OutOfStock") > 0:
    for i in range(len(gifts_list)):
      if gifts_list[i] == command[1]:
        gifts_list[i] = "None"
  elif command.count("Required") > 0:
        gifts_list[int(command[2])] = command[1]
  elif command.count("JustInCase") > 0:
        gifts_list[-1] = command[1]
  command = input()
  if command == "No Money":
      for j in range(len(command)):
        if command[j] == "None":
            gifts_list.remove(command[j]) 
      break  
  
print(" ".join(gifts_list))
