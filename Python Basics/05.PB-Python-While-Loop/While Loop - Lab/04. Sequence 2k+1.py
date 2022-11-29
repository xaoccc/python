#user input
number = int(input())
#define the current number we will check
current_number = 1

#logic and output
while current_number <= number :
#The first thing in the loop we do is do something with the current number we defined
    print(current_number)
#Then we change its value and then the loop checks if the conditions meet, if yes - the loop continues, if no - it stops before printing/using the next one. If we put the print() below the calculations, the program returns one more value, which we do not need.
    current_number = 2 * current_number + 1