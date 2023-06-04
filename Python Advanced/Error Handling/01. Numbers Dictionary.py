numbers_dictionary = {}
line = input()

while line != "Search":
    try:
        number = int(input())
        numbers_dictionary[line] = number
    except ValueError:
        print("The variable number must be an integer")
    line = input()


line = input()    
while line != "Remove":
    searched = line
    try:
        print(numbers_dictionary[searched])
    except KeyError:
        print("Number does not exist in dictionary")
    line = input()
    
line = input()    
while line != "End":
    searched = line
    try:
        del numbers_dictionary[searched]
    except KeyError:
        print("Number does not exist in dictionary")
    line = input()
print(numbers_dictionary)
