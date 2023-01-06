#src: https://python-book.softuni.bg/chapter-09-problems-for-champions-part-2.html

problem = input()
total = 0
result = 0
internal_result = 0
internal = False
operator = ""

for i in range(0, len(problem) - 1):
    if i == 1 and problem[0] != "(":
        result = int(problem[0])
    
    if problem[i] == "+":
        if internal == True:
            internal_result += int(problem[i+1])
        else:
            result += int(problem[i+1])
        i += 1
    elif problem[i] == "-": 
        result -= int(problem[i+1])
        if internal == True:
            internal_result -= int(problem[i+1])
        i += 1
    elif problem[i] == "/": 
        result /= int(problem[i+1])
        if internal == True:
            internal_result /= int(problem[i+1])
        i += 1
    elif problem[i] == "*": 
        result *= int(problem[i+1])
        if internal == True:
            internal_result *= int(problem[i+1])
        i += 1
        
    elif problem[i] == "(":
        if i > 0:
            operator = problem[i-1]
        internal = True
        internal_result = int(problem[i+1])
    elif problem[i] == ")":
        internal = False
        if operator == "+":
            result += internal_result
        elif operator == "-":
            result -= internal_result
        elif operator == "/":
            result /= internal_result
        elif operator == "*":
            result *= internal_result
        else:
            result = internal_result
        
        
            
        
    print(result)
        

            

