#Split the str output into a list
courses_list = input().split(", ")
command = input()

#the break condition is in the loop
while command != "course start":
  #Starting with the commands and converting them into lists
    command = command.split(":")
    #Creating a variable for the exercises, not including swap cases, because swap command has index 2, here we would receive an index-out-of-range error for the other commands
    exercise = command[1] + "-Exercise"
    
    #Command 1 - "Add" is very somple and we use append() method
    if command[0] == "Add":
        if command[1] not in courses_list:
            courses_list.append(command[1])
            
    #Command 2 - "Insert": we use insert() method, be careful to convert the second number in the command into int : int(command[2])
    elif command[0] == "Insert":
        if command[1] not in courses_list:
            courses_list.insert(int(command[2]), command[1])
            
    #Command 3 - "Remove": We remove the course and if there is also an exercise, don't forget to remove it too
    elif command[0] == "Remove":
        courses_list.remove(command[1])
        if exercise in courses_list:
            courses_list.remove(command[1])
            
    #Command 4 - "Swap": The most difficult command 
    elif command[0] == "Swap": 
      
        #1. We create a variable for the exercise of the second course(we already have one for the first exercise)
        swap_exercise = command[2] + "-Exercise"
        
        #2. Checking if both courses exist
        if command[1] in courses_list and command[2] in courses_list:
          
            #3. We find the index of each course
            idx1 = courses_list.index(command[1])
            idx2 = courses_list.index(command[2])
            
            #4. Spat the courses
            courses_list[idx1], courses_list[idx2] = courses_list[idx2], courses_list[idx1]
            
            #5. If both courses exist, we just spat the exercises:
            if exercise in courses_list and swap_exercise in courses_list:
                courses_list[idx1 + 1], courses_list[idx2 + 1] = courses_list[idx2 + 1], courses_list[idx1 + 1]
                
            #6. If just the first exercise exists, we put it next after the course: idx2 + 1. Remember we already swapped the courses, so here we use the index of the second course, knowing that there is already the first one    
            elif exercise in courses_list:
                ex1_idx = courses_list.index(command[2]) + 1
                courses_list.insert(idx2 + 1, exercise)
                del courses_list[ex1_idx + 1]
              
            #7. Here we are checking just for the second exercise and do the same as for the first one 
            elif swap_exercise in courses_list:
                ex2_idx = courses_list.index(command[1]) + 1
                courses_list.insert(idx1 + 1, swap_exercise)
                del courses_list[ex2_idx + 1]
                
    #Command 5 - "Exercise"        
    elif command[0] == "Exercise":
      
        #First we check if the course is available and there is no exercise. If this is the case, we siply add an exercise next to the course
        if command[1] in courses_list and exercise not in courses_list:
            exercise_idx = courses_list.index(command[1]) + 1
            courses_list.insert(exercise_idx, exercise)
            
        #If there is no course, there is no exercise for sure, so we add first thecourse, then the exercise at the end of the list, using append() again
        if command[1] not in courses_list:
            courses_list.append(command[1])
            courses_list.append(exercise)

    command = input()

#The output is also tricky. We must print each course on a new line and write the number(not the index) in front of the name. 
#If we start counting from 1, this will not work, because either the index will be out of range (len(courses_list)+1), or we will not print the last course.
#Because we are clever, we will write i+1 inside the print() and everything will be OK :)
for i in range(len(courses_list)):
    print(f"{i+1}.{courses_list[i]}")
